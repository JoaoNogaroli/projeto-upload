
def teste_download(user_uid, file_name):
    import pyrebase
    import pandas as pd
    import os
    import webbrowser

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
    storage  = firebase.storage()
    print('OK')
    arquivo = storage.child("File").child("user:_"+user_uid).child(file_name)
    url = arquivo.get_url(None)
    print(arquivo)
    print(url)
    storage.child("File").child("user:_"+user_uid).child(file_name).download("local.csv")
    # ESSE COMANDO FAZ O DOWNLOAD!!!!!
    #---->>>>>>>>>>>>.    #teste = webbrowser.open(url)
    #------
    #valor.download(filename="arq.csv")