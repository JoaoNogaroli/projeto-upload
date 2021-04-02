from flask import Flask, request, render_template, redirect, render_template_string, make_response
import os
import pyrebase
from cadastro import func_cadastrar
from salvar import salvar
from download import teste_download
import pandas as pd

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
    try:
        df = teste_download(user_uid, file_name)
        resp = make_response(render_template_string(df.to_html()))
        return resp
    except Exception as e:
        print(e)
        return "ERROR"

@app.route("/visualizar")
def pag_visualizar():
    return render_template("visualizar.html")

if __name__ == "__main__":
    app.run(debug=True, port=port)