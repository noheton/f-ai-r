<#
.SYNOPSIS
    Generates a report about files in a directory without following symbolic links or reparse points.

.DESCRIPTION
    Recursively enumerates files in the specified directory, skipping symbolic links,
    junctions, and other reparse points. Produces a summary (total count, total size,
    extension breakdown, largest files, newest/oldest files) and a per-file listing.
    Output can be written to the console, a text file, or CSV.

.PARAMETER Path
    The directory to scan. Defaults to the current directory.

.PARAMETER OutputFile
    Optional path to write the human-readable report to. If omitted, the report is
    written to the console.

.PARAMETER CsvFile
    Optional path to write the per-file listing as CSV.

.PARAMETER TopN
    Number of entries to include in "largest files" and "extension breakdown" sections.
    Defaults to 10.

.EXAMPLE
    .\Get-DirectoryReport.ps1 -Path C:\Projects -OutputFile report.txt -CsvFile files.csv
#>

[CmdletBinding()]
param(
    [Parameter(Position = 0)]
    [string]$Path = (Get-Location).Path,

    [string]$OutputFile,

    [string]$CsvFile,

    [int]$TopN = 10
)

if (-not (Test-Path -LiteralPath $Path -PathType Container)) {
    throw "Directory not found: $Path"
}

$resolved = (Resolve-Path -LiteralPath $Path).Path

function Test-IsReparsePoint {
    param([System.IO.FileSystemInfo]$Item)
    return ($Item.Attributes -band [System.IO.FileAttributes]::ReparsePoint) -eq [System.IO.FileAttributes]::ReparsePoint
}

# Manual recursion so we can skip reparse-point directories outright.
function Get-FilesNoFollow {
    param([string]$Root)

    $stack = [System.Collections.Generic.Stack[string]]::new()
    $stack.Push($Root)

    while ($stack.Count -gt 0) {
        $current = $stack.Pop()
        try {
            $entries = Get-ChildItem -LiteralPath $current -Force -ErrorAction Stop
        } catch {
            Write-Warning "Cannot read '$current': $($_.Exception.Message)"
            continue
        }

        foreach ($entry in $entries) {
            if (Test-IsReparsePoint -Item $entry) {
                Write-Verbose "Skipping reparse point: $($entry.FullName)"
                continue
            }
            if ($entry.PSIsContainer) {
                $stack.Push($entry.FullName)
            } else {
                $entry
            }
        }
    }
}

Write-Verbose "Scanning $resolved (not following links)"
$files = @(Get-FilesNoFollow -Root $resolved)

$totalCount = $files.Count
$totalSize  = ($files | Measure-Object -Property Length -Sum).Sum
if (-not $totalSize) { $totalSize = 0 }

$byExt = $files |
    Group-Object { if ($_.Extension) { $_.Extension.ToLowerInvariant() } else { '(none)' } } |
    ForEach-Object {
        [pscustomobject]@{
            Extension = $_.Name
            Count     = $_.Count
            Bytes     = ($_.Group | Measure-Object -Property Length -Sum).Sum
        }
    } |
    Sort-Object Bytes -Descending

$largest = $files | Sort-Object Length -Descending | Select-Object -First $TopN
$newest  = $files | Sort-Object LastWriteTime -Descending | Select-Object -First 1
$oldest  = $files | Sort-Object LastWriteTime | Select-Object -First 1

function Format-Size {
    param([double]$Bytes)
    $units = 'B','KB','MB','GB','TB','PB'
    $i = 0
    while ($Bytes -ge 1024 -and $i -lt $units.Count - 1) {
        $Bytes /= 1024
        $i++
    }
    '{0,8:N2} {1}' -f $Bytes, $units[$i]
}

$sb = [System.Text.StringBuilder]::new()
[void]$sb.AppendLine("Directory report")
[void]$sb.AppendLine("================")
[void]$sb.AppendLine("Path       : $resolved")
[void]$sb.AppendLine("Generated  : $(Get-Date -Format o)")
[void]$sb.AppendLine("Host       : $([System.Environment]::MachineName)")
[void]$sb.AppendLine("Files      : $totalCount")
[void]$sb.AppendLine("Total size : $(Format-Size $totalSize) ($totalSize bytes)")
[void]$sb.AppendLine("Note       : symbolic links / junctions / reparse points were not followed")
[void]$sb.AppendLine()

[void]$sb.AppendLine("Top $TopN extensions by size")
[void]$sb.AppendLine("---------------------------")
foreach ($row in ($byExt | Select-Object -First $TopN)) {
    [void]$sb.AppendLine(('{0,-12} {1,8} files  {2}' -f $row.Extension, $row.Count, (Format-Size $row.Bytes)))
}
[void]$sb.AppendLine()

[void]$sb.AppendLine("Top $TopN largest files")
[void]$sb.AppendLine("-----------------------")
foreach ($f in $largest) {
    [void]$sb.AppendLine(('{0}  {1}' -f (Format-Size $f.Length), $f.FullName))
}
[void]$sb.AppendLine()

if ($newest) {
    [void]$sb.AppendLine("Newest file: $($newest.LastWriteTime.ToString('o'))  $($newest.FullName)")
}
if ($oldest) {
    [void]$sb.AppendLine("Oldest file: $($oldest.LastWriteTime.ToString('o'))  $($oldest.FullName)")
}

$report = $sb.ToString()

if ($OutputFile) {
    $report | Set-Content -LiteralPath $OutputFile -Encoding UTF8
    Write-Host "Report written to $OutputFile"
} else {
    Write-Output $report
}

if ($CsvFile) {
    $files |
        Select-Object FullName, Length, LastWriteTime, CreationTime, Attributes |
        Export-Csv -LiteralPath $CsvFile -NoTypeInformation -Encoding UTF8
    Write-Host "Per-file CSV written to $CsvFile"
}
