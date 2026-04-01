/* Service Worker — Dataset Cadaster PWA */
var CACHE_NAME = 'dataset-cadaster-v1';
var HTML_ASSETS = [
  'index.html',
  'landing.html',
  'estimator.html'
];
var JSON_ASSETS = [
  '../datasets.json'
];
var ALL_ASSETS = HTML_ASSETS.concat(JSON_ASSETS);

/* Install — pre-cache core assets */
self.addEventListener('install', function(e) {
  e.waitUntil(
    caches.open(CACHE_NAME).then(function(cache) {
      return cache.addAll(ALL_ASSETS);
    }).then(function() {
      return self.skipWaiting();
    })
  );
});

/* Activate — clean old caches */
self.addEventListener('activate', function(e) {
  e.waitUntil(
    caches.keys().then(function(names) {
      return Promise.all(
        names.filter(function(n) { return n !== CACHE_NAME; })
             .map(function(n) { return caches.delete(n); })
      );
    }).then(function() {
      return self.clients.claim();
    })
  );
});

/* Fetch — strategy depends on resource type */
self.addEventListener('fetch', function(e) {
  var url = new URL(e.request.url);

  /* Only handle same-origin GET requests */
  if (e.request.method !== 'GET' || url.origin !== self.location.origin) return;

  var isJSON = url.pathname.endsWith('.json') && !url.pathname.endsWith('manifest.json');

  if (isJSON) {
    /* Network-first for JSON data (fresh data when online) */
    e.respondWith(
      fetch(e.request).then(function(response) {
        var clone = response.clone();
        caches.open(CACHE_NAME).then(function(cache) {
          cache.put(e.request, clone);
        });
        return response;
      }).catch(function() {
        return caches.match(e.request);
      })
    );
  } else {
    /* Cache-first for HTML and other assets */
    e.respondWith(
      caches.match(e.request).then(function(cached) {
        if (cached) {
          /* Update cache in background */
          fetch(e.request).then(function(response) {
            caches.open(CACHE_NAME).then(function(cache) {
              cache.put(e.request, response);
            });
          }).catch(function() {});
          return cached;
        }
        return fetch(e.request).then(function(response) {
          var clone = response.clone();
          caches.open(CACHE_NAME).then(function(cache) {
            cache.put(e.request, clone);
          });
          return response;
        });
      })
    );
  }
});
