var serviceWorkerSrc = "/static/js/sw.js";
var callhome = function(status) {
  console.log(status);
}
var storage = window.localStorage;
var registration;
const publicKey = 'BEWS1IhTcSVb7XhvP-5yeE0Zhl-F0iCB1TN3m8JSBH2Gi-cUzMQ2DXeON-T8BiF1_1gQOb8YMncdwRZfp3BsIW8';

function urlB64ToUint8Array(base64String) {
  const padding = '='.repeat((4 - base64String.length % 4) % 4);
  const base64 = (base64String + padding)
    .replace(/\-/g, '+')
    .replace(/_/g, '/');

  const rawData = window.atob(base64);
  const outputArray = new Uint8Array(rawData.length);

  for (let i = 0; i < rawData.length; ++i) {
    outputArray[i] = rawData.charCodeAt(i);
  }
  return outputArray;
}

//Checks if the browser support service workers
function onPageLoad() {
 // Do everything if the Browser Supports Service Worker
 if ('serviceWorker' in navigator) {
   navigator.serviceWorker.register(serviceWorkerSrc)
     .then(
       function(reg) {
         registration = reg;
         initialiseState(reg);
       }
     );
 }
 // If service worker not supported, show warning to the message box
 else {
   callhome("service-worker-not-supported");
 }
}

// Once the service worker is registered set the initial state
function initialiseState(reg) {
 // Are Notifications supported in the service worker?
 if (!(reg.showNotification)) {
   callhome("showing-notifications-not-supported-in-browser");
   return;
 }
 // Check the current Notification permission.
 if (Notification.permission === 'denied') {
   callhome("notifications-disabled-by-user");
   return;
 }
 // Check if push messaging is supported
 if (!('PushManager' in window)) {
   // Show a message and activate the button
   console.log('push-notifications-not-supported-in-browser');
   return;
 }
 subscribe();
}

/*navigator.serviceWorker && navigator.serviceWorker.ready.then(function(serviceWorkerRegistration) {  
  serviceWorkerRegistration.pushManager.getSubscription()  
    .then(function(subscription) {  
      if (subscription) {
        console.info('Got existing', subscription);
        window.subscription = subscription;
        return;  // got one, yay
      }

      const applicationServerKey = urlB64ToUint8Array(publicKey);
      serviceWorkerRegistration.pushManager.subscribe({
          userVisibleOnly: true,
          applicationServerKey,
      })
        .then(function(subscription) { 
          console.info('Newly subscribed to push!', subscription);
          window.subscription = subscription;
        });
    });
});*/

function subscribe() {
 registration.pushManager.getSubscription().then(
     function(existing_subscription) {
       // Check if Subscription is available
       if (existing_subscription) {
         endpoint = existing_subscription.toJSON()['endpoint']
         if (storage.getItem(endpoint) === 'failed') {
           postSubscribeObj('subscribe', existing_subscription);
         }
         return existing_subscription;
       }
       // If not, register one using the
       // registration object we got when
       // we registered the service worker
       registration.pushManager.subscribe({
         userVisibleOnly: true
       }).then(
         function(new_subscription) {
           postSubscribeObj('subscribe', new_subscription);
         }
       );
     }
   )
}

function unsubscribe() {
 navigator.serviceWorker.ready.then(function(existing_reg) {
   // Get the Subscription to unregister
   registration.pushManager.getSubscription()
     .then(
       function(subscription) {
         // Check we have a subscription to unsubscribe
         if (!subscription) {
           return;
         }
         postSubscribeObj('unsubscribe', subscription);
       }
     )
 });
}

function postSubscribeObj(statusType, subscription) {
 // Send the information to the server with fetch API.
 // the type of the request, the name of the user subscribing,
 // and the push subscription endpoint + key the server needs
 // to send push messages
 var subscription = subscription.toJSON();
 // API call to store the endpoint in the database
}

onPageLoad();