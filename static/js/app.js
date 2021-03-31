var firebaseConfig = {
    apiKey: "AIzaSyC2sj1gQU0lSPY8tlnsCsP9bFEXEfx69ec",
    authDomain: "files-b6c7a.firebaseapp.com",
    projectId: "files-b6c7a",
    databaseURL: "https://files-b6c7a-default-rtdb.firebaseio.com/",
    storageBucket: "files-b6c7a.appspot.com",
    messagingSenderId: "50138812088",
    appId: "1:50138812088:web:46f495270f77fea4076e4d",
    measurementId: "G-GQ02V07392"
};

var firebase = firebase.initializeApp(firebaseConfig);
firebase.analytics();
var storage = firebase.storage();
var storageRef = storage.ref();

