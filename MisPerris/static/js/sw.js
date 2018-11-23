var CACHE_NAME = 'misperris-cache';

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll([
        		'/',
        		//'/quienes_somos'
        	]);
      })
  );
});

self.addEventListener('fetch', function(event) {
  var requestUrl = new URL(event.request.url);
    if (requestUrl.origin === location.origin) {
      if ((requestUrl.pathname === '/')) {
        event.respondWith(caches.match(event.request));
        return;
      }
    }
  event.respondWith(
      caches.match(event.request).then(function(response) {
        return response || fetch(event.request);
      })
    );
});

//${event.data.text()}	

// Register event listener for the 'push' event.
self.addEventListener('push', function(event) {
	payload = event.data.text();
	// Keep the service worker alive until the notification is created.
	event.waitUntil(
		// Show a notification with title and use the payload
		// as the body.
		self.registration.showNotification(payload.title, payload.options)
 );
});

self.addEventListener('notificationclick', function(event) {
  console.log('[Service Worker] Notification click Received.');
  event.notification.close();
  event.waitUntil(
    clients.openWindow('https://critoblue.pythonanywhere.com')
  );
});