self.addEventListener("install", e => {
  e.waitUntil(
    caches.open("luna-cache").then(cache => {
      return cache.addAll(["/", "/static/style.css"]);
    })
  );
});

self.addEventListener("fetch", e => {
  e.respondWith(
    caches.match(e.request).then(response => {
      return response || fetch(e.request);
    })
  );
});
