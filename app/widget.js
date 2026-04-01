/* Dataset Cadaster — Embeddable Widget
   Usage:
   <div id="dataset-cadaster-widget" data-category="dem-elevation" data-max="5"></div>
   <script src="widget.js"></script>
*/
(function() {
  'use strict';

  var container = document.getElementById('dataset-cadaster-widget');
  if (!container) return;

  var category = container.getAttribute('data-category') || '';
  var maxItems = parseInt(container.getAttribute('data-max'), 10) || 10;

  /* Determine base URL from the script src */
  var scripts = document.getElementsByTagName('script');
  var baseUrl = '';
  for (var i = 0; i < scripts.length; i++) {
    var src = scripts[i].src || '';
    if (src.indexOf('widget.js') !== -1) {
      baseUrl = src.replace(/\/app\/widget\.js.*$/, '');
      break;
    }
  }

  var COST_COLORS = {
    free:       { bg: '#e8f8f0', fg: '#27ae60' },
    freemium:   { bg: '#fdf3e6', fg: '#e67e22' },
    commercial: { bg: '#fbeaea', fg: '#c0392b' }
  };

  var CAT_COLOR = '#2980b9';

  /* Inject scoped styles */
  var style = document.createElement('style');
  style.textContent = [
    '#dataset-cadaster-widget{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;max-width:640px;border:1px solid #dce1e8;border-radius:8px;background:#fff;overflow:hidden}',
    '#dataset-cadaster-widget *{box-sizing:border-box;margin:0;padding:0}',
    '.dcw-hdr{background:#1a2634;color:#fff;padding:12px 16px;font-size:14px;font-weight:600;display:flex;align-items:center;gap:6px}',
    '.dcw-hdr span{color:#5dade2}',
    '.dcw-list{list-style:none;padding:0;margin:0}',
    '.dcw-item{padding:12px 16px;border-bottom:1px solid #eef0f3;display:flex;flex-direction:column;gap:6px}',
    '.dcw-item:last-child{border-bottom:none}',
    '.dcw-row{display:flex;align-items:center;gap:8px;flex-wrap:wrap}',
    '.dcw-name{font-size:14px;font-weight:600;color:#2980b9;text-decoration:none}',
    '.dcw-name:hover{text-decoration:underline}',
    '.dcw-badge{font-size:11px;padding:2px 8px;border-radius:10px;font-weight:600;white-space:nowrap}',
    '.dcw-desc{font-size:12px;color:#5a6a7a;line-height:1.4;display:-webkit-box;-webkit-line-clamp:1;-webkit-box-orient:vertical;overflow:hidden}',
    '.dcw-footer{padding:10px 16px;background:#f7f8fa;text-align:center}',
    '.dcw-footer a{color:#2980b9;font-size:13px;font-weight:600;text-decoration:none}',
    '.dcw-footer a:hover{text-decoration:underline}',
    '.dcw-empty{padding:24px 16px;text-align:center;color:#5a6a7a;font-size:13px}',
    '@media(max-width:480px){.dcw-item{padding:10px 12px}.dcw-hdr{padding:10px 12px}}'
  ].join('\n');
  document.head.appendChild(style);

  /* Render loading state */
  container.innerHTML = '<div class="dcw-hdr"><span>&#9672;</span> Dataset Cadaster</div><div class="dcw-empty">Loading datasets...</div>';

  /* Fetch data */
  var jsonUrl = baseUrl + '/datasets-summary.json';
  var xhr = new XMLHttpRequest();
  xhr.open('GET', jsonUrl, true);
  xhr.onload = function() {
    if (xhr.status >= 200 && xhr.status < 300) {
      try {
        var data = JSON.parse(xhr.responseText);
        var datasets = Array.isArray(data) ? data : (data.datasets || []);
        render(datasets);
      } catch (e) {
        showError('Failed to parse data');
      }
    } else {
      showError('Failed to load datasets');
    }
  };
  xhr.onerror = function() { showError('Network error'); };
  xhr.send();

  function render(datasets) {
    /* Filter by category if specified */
    if (category) {
      datasets = datasets.filter(function(d) { return d.category === category; });
    }

    /* Limit */
    datasets = datasets.slice(0, maxItems);

    if (datasets.length === 0) {
      container.innerHTML = '<div class="dcw-hdr"><span>&#9672;</span> Dataset Cadaster</div><div class="dcw-empty">No datasets found</div>';
      return;
    }

    var items = datasets.map(function(d) {
      var costStyle = COST_COLORS[d.cost] || COST_COLORS.free;
      var catLabel = (d.category || '').replace(/-/g, ' ');
      return '<li class="dcw-item">' +
        '<div class="dcw-row">' +
          '<a class="dcw-name" href="' + esc(d.url) + '" target="_blank" rel="noopener">' + esc(d.name) + '</a>' +
          '<span class="dcw-badge" style="background:' + CAT_COLOR + '22;color:' + CAT_COLOR + '">' + esc(catLabel) + '</span>' +
          '<span class="dcw-badge" style="background:' + costStyle.bg + ';color:' + costStyle.fg + '">' + esc(d.cost || 'free') + '</span>' +
        '</div>' +
        '<div class="dcw-desc">' + esc(d.description || '') + '</div>' +
      '</li>';
    }).join('');

    var catalogUrl = baseUrl + '/app/index.html' + (category ? '#category=' + category : '');

    container.innerHTML =
      '<div class="dcw-hdr"><span>&#9672;</span> Dataset Cadaster</div>' +
      '<ul class="dcw-list">' + items + '</ul>' +
      '<div class="dcw-footer"><a href="' + esc(catalogUrl) + '" target="_blank" rel="noopener">View full catalog &rarr;</a></div>';
  }

  function showError(msg) {
    container.innerHTML = '<div class="dcw-hdr"><span>&#9672;</span> Dataset Cadaster</div><div class="dcw-empty">' + esc(msg) + '</div>';
  }

  function esc(s) {
    var d = document.createElement('div');
    d.appendChild(document.createTextNode(s));
    return d.innerHTML;
  }
})();
