/* ══════════════════════════════════════════════════════════
   Dataset Cadaster — Shared JavaScript
   Common JS extracted from all pages to reduce duplication.
   ══════════════════════════════════════════════════════════ */

/* ── Dark Mode Init / Toggle / Persist ───────────────── */
(function(){
  var saved = localStorage.getItem('dc-theme');
  if (saved === 'dark') {
    document.documentElement.setAttribute('data-theme', 'dark');
  }
})();

function dcToggleDark() {
  var current = document.documentElement.getAttribute('data-theme') === 'dark';
  var next = current ? '' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('dc-theme', next ? 'dark' : 'light');
  return next;
}

/* ── Theme Sync Across Pages ─────────────────────────── */
window.addEventListener('storage', function(e) {
  if (e.key === 'dc-theme') {
    document.documentElement.setAttribute('data-theme', e.newValue === 'dark' ? 'dark' : '');
  }
});

/* ── HTML Escape ─────────────────────────────────────── */
function esc(s) {
  var d = document.createElement('div');
  d.appendChild(document.createTextNode(s || ''));
  return d.innerHTML;
}

/* ── Format Category String ──────────────────────────── */
function formatCategory(c) {
  if (!c) return '';
  return c.replace(/-/g, ' ').replace(/\b\w/g, function(l) { return l.toUpperCase(); })
          .replace(/\bEo\b/, 'EO').replace(/\bDem\b/, 'DEM').replace(/\bInsar\b/, 'InSAR');
}

/* ── Toast Notification ──────────────────────────────── */
var _dcToastTimer = null;
function showToast(msg) {
  var el = document.querySelector('.toast');
  if (!el) {
    el = document.createElement('div');
    el.className = 'toast';
    document.body.appendChild(el);
  }
  el.textContent = msg;
  el.classList.add('show');
  clearTimeout(_dcToastTimer);
  _dcToastTimer = setTimeout(function() { el.classList.remove('show'); }, 2000);
}
