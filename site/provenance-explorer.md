# Provenance explorer

The PROV-O graph at [`doc/provenance.ttl`](https://github.com/noheton/f-ai-r/blob/main/doc/provenance.ttl)
rendered as an interactive node-link diagram. Filter by class, search by
label or IRI, and click any node to inspect its outgoing relations.

<div class="prov-controls">
  <label>Filter:
    <select id="prov-filter">
      <option value="all">All classes</option>
      <option value="agent">Agents</option>
      <option value="activity">Activities</option>
      <option value="entity">Entities</option>
      <option value="claim">Claims</option>
      <option value="source">Sources</option>
      <option value="prompt">Prompts</option>
    </select>
  </label>
  <label>Search:
    <input type="text" id="prov-search" placeholder="label or IRI fragment">
  </label>
  <span id="prov-count" class="muted"></span>
</div>

<div id="prov-explorer"></div>

<div class="prov-info" id="prov-info">
Click a node above to see its label, type, and outgoing edges.
</div>

<script src="https://unpkg.com/vis-network@9.1.9/standalone/umd/vis-network.min.js"></script>
<script>
(async function() {
  const res = await fetch('static/provenance.json');
  if (!res.ok) {
    document.getElementById('prov-explorer').innerHTML =
      '<p style="padding:24px">Provenance graph data not available. Rebuild the site with <code>python scripts/build_provenance_site.py</code>.</p>';
    return;
  }
  const data = await res.json();
  const colorByClass = {
    agent:    '#82a043',  // DLR green
    activity: '#00658b',  // DLR blue
    entity:   '#666666',  // DLR mid-grey
    claim:    '#d2ae3d',  // DLR yellow
    source:   '#0094a8',  // DLR teal
    prompt:   '#5f98cb',  // DLR sky
    other:    '#b1b1b1'
  };
  const allNodes = data.nodes.map(n => ({
    id: n.id,
    label: n.label.length > 32 ? n.label.slice(0,30) + '…' : n.label,
    title: `${n.label}\n${n.iri}\nclass: ${n.cls}`,
    iri: n.iri,
    cls: n.cls,
    fullLabel: n.label,
    color: { background: colorByClass[n.cls] || colorByClass.other,
             border: '#333' },
    font: { color: '#fff', face: 'Arial', size: 13 },
    shape: n.cls === 'claim' ? 'box' : (n.cls === 'activity' ? 'ellipse' : 'dot'),
    margin: 8
  }));
  const allEdges = data.edges.map(e => ({
    from: e.from, to: e.to, label: e.label,
    color: { color: '#cfcfcf', highlight: '#00658b' },
    font: { size: 10, color: '#666', face: 'Arial', align: 'middle' },
    arrows: 'to', smooth: { type: 'cubicBezier' }
  }));

  let nodes = new vis.DataSet(allNodes);
  let edges = new vis.DataSet(allEdges);
  const container = document.getElementById('prov-explorer');
  const network = new vis.Network(container, { nodes, edges }, {
    physics: { stabilization: { iterations: 250 },
               barnesHut: { gravitationalConstant: -7000,
                            centralGravity: 0.3, springLength: 130 } },
    interaction: { hover: true, tooltipDelay: 100 },
    edges: { arrows: { to: { scaleFactor: 0.5 } } }
  });

  function applyFilter() {
    const cls = document.getElementById('prov-filter').value;
    const q = document.getElementById('prov-search').value.toLowerCase();
    const keep = allNodes.filter(n =>
      (cls === 'all' || n.cls === cls) &&
      (!q || n.fullLabel.toLowerCase().includes(q) || n.iri.toLowerCase().includes(q))
    );
    const keepIds = new Set(keep.map(n => n.id));
    nodes.clear();
    nodes.add(keep);
    edges.clear();
    edges.add(allEdges.filter(e => keepIds.has(e.from) && keepIds.has(e.to)));
    document.getElementById('prov-count').textContent =
      `${keep.length} nodes, ${edges.length} edges`;
  }
  document.getElementById('prov-filter').addEventListener('change', applyFilter);
  document.getElementById('prov-search').addEventListener('input', applyFilter);
  applyFilter();

  network.on('click', params => {
    const info = document.getElementById('prov-info');
    if (params.nodes.length === 0) {
      info.innerHTML = 'Click a node above to see its label, type, and outgoing edges.';
      return;
    }
    const id = params.nodes[0];
    const node = allNodes.find(n => n.id === id);
    const out = allEdges.filter(e => e.from === id);
    let html = `<strong>${node.fullLabel}</strong><br>`;
    html += `<code>${node.iri}</code> &middot; class: <strong>${node.cls}</strong><br>`;
    if (out.length) {
      html += `<br>Outgoing relations (${out.length}):<ul>`;
      for (const e of out) {
        const target = allNodes.find(n => n.id === e.to);
        html += `<li><code>${e.label}</code> &rarr; ${target ? target.fullLabel : e.to}</li>`;
      }
      html += '</ul>';
    } else {
      html += '<br>No outgoing edges.';
    }
    info.innerHTML = html;
  });
})();
</script>
