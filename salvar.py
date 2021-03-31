import pyrebase
import datetime
import random
import time

def salvar(user_id,name, file_to_save):        
    config = {
        'apiKey': "AIzaSyC2sj1gQU0lSPY8tlnsCsP9bFEXEfx69ec",
        'authDomain': "files-b6c7a.firebaseapp.com",
        'projectId': "files-b6c7a",
        'databaseURL': "https://files-b6c7a-default-rtdb.firebaseio.com/",
        'storageBucket': "files-b6c7a.appspot.com",
        'messagingSenderId': "50138812088",
        'appId': "1:50138812088:web:46f495270f77fea4076e4d",
        'measurementId': "G-GQ02V07392"
    };
    firebase = pyrebase.initialize_app(config)
    database = firebase.database()
    storage = firebase.storage()

    storage.child("File").child("user:_"+user_id+"/"+name).put(file_to_save)


