self.addEventListener('install', (event) => {
  self.skipWaiting();
  console.log('Service Worker installed.');
});

self.addEventListener('fetch', (event) => {
  // Intentionally minimal.
});
