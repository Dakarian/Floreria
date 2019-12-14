var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
  '/',
  '/static/core/css/estilos_floreria.css',
  '/galeria',
  '/carrito',
  '/quienes_somos',
];

self.addEventListener('install', function (event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function (cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function (event) {
  event.respondWith(
    caches.match(event.request).then(function (response) {

      return fetch(event.request)
        .catch(function (rsp) {
          return response;
        });


    })
  );
});


// codigo para notificaciones push

importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

var firebaseConfig = {
  apiKey: "AIzaSyCa15wmnJ6thDGRSHzwFHebmehD_0Do1-E",
  authDomain: "petalosfloreria0.firebaseapp.com",
  databaseURL: "https://petalosfloreria0.firebaseio.com",
  projectId: "petalosfloreria0",
  storageBucket: "petalosfloreria0.appspot.com",
  messagingSenderId: "890461962388",
  appId: "1:890461962388:web:b9ee44c096ae0fae83b481"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

let messaging = firebase.messaging();

messaging.setBackgroundMessageHandler(function (payload) {
  let title = 'titulo de la notificacion';

  let options = {
    body: 'este es el mensaje',
    icon: '/static/core/img/logo.jpg'
  }

  self.registration.showNotification(title, options);
});