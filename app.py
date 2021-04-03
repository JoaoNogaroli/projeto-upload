from flask import Flask, request, render_template, redirect, render_template_string, make_response
import os
import pyrebase
from cadastro import func_cadastrar
from salvar import salvar
from download import teste_download
import pandas as pd
import csv


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
storage = firebase.storage()


app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/pag_cad")
@app.route("/pag_cad", methods=['POST'])
def pag_cad():
    return render_template('pag_cad.html')
#app.config['FILE_UPLOADS'] = '*\\static\\files'

@app.route("/user_logged")
def user_logged():
    return render_template ("user_logged.html")

@app.route("/realizar_cadastro", methods=['POST'])
def realizar_cadastro():
    email = request.form['email']
    senha = request.form['senha']
    try:
        func_cadastrar(email, senha)
        fim = "Cadastrado com sucesso!  " + email
        return render_template('index.html', email=fim)
    except:
        fim = "Email já cadastrado"
        return render_template('pag_cad.html', fim=fim)

app.config["ALLOWED_FILE_EXTENSIONS"] = ["XLSX","XLRD", "CSV"]

def allow(filename):
    if not "." in filename:
        return False
    
    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_FILE_EXTENSIONS"]:
        return True
    else:
        return False

@app.route("/upload", methods=["POST"])
def upload_file():
    if request.method == 'POST':
        if request.files:
            file_to_save = request.files['file']
            #image.save(os.path.join(app.config['FILE_UPLOADS'], image.filename))
            user_id = request.form['user_id']
            print(user_id)
            print(file_to_save)
            fim = "Arquivo enviado com sucesso"
            error_ext ="Extensão inválida, envie arquivos .xlsx ou .csv"
            if not allow(file_to_save.filename):
                print("EXTENSAO ERROR")
                return render_template('user_logged.html', fim=error_ext)
            else:
                salvar(user_id, file_to_save.filename, file_to_save)
                return render_template('user_logged.html', fim=fim)

@app.route("/analise_escolhido", methods=["POST"])
def download():
    user_uid = request.form['user_id_dois']
    file_name = request.form['filename']
    print(user_uid + "_e_ " + file_name)
    print('1   -------')
    try:
        results = []
        items= []
        df = teste_download(user_uid, file_name)
        dfdi= df.to_dict()
        print(df)
        print('1--------DICIONARIO------')

        for colum in dfdi.keys():
            results.append(colum) 

        for row in dfdi:
            items.append(dfdi[row])

        #print(results)
        print('2--------Lista com os Results------')

        #print(df[results[1]])
        #print("Quantidade de linhas "+str(len(df[results[0]])))
        print('3--------Teste------')

        quantidade_rows = df.shape[0]
        #print(df.shape[0])
        #print('4--------Teste  2------')
       #print(items)
        print('5--------Teste  3------')
        #for row in items:
        #    print(row)
            
            #for index in range(0,len(results)-1):
                
                #print(row[results[index]])
        '''print(items[0][0])
        print(items[1][0])
        print(items[2][0])
        print(items[3][0])
        print(items[4][0])'''

        print('6--------Teste  4------')
        #for row in items:
       #    # print(row)
        #    for i in row:
             #   print(row[i])
        """print('7--------Teste 5------')
        print(items[0])
        print('8--------Teste6------')
        print(items[0][0])
        print('9--------Teste 8------')
        print(items[6])
        print('8--------Teste 9------')
        print(items[6][0])"""


        return render_template('teste.html', results=results,items=items, quantidade_rows=quantidade_rows, df=df, len=len)
    except Exception as e:
        print(e)
        return "ERROR"

@app.route("/visualizar")
def pag_visualizar():
    return render_template("visualizar.html")

if __name__ == "__main__":
    app.run(debug=True, port=port)