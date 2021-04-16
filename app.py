from flask import Flask, request, render_template, redirect, render_template_string, make_response, url_for, session
import os
import pyrebase
from cadastro import func_cadastrar
from salvar import salvar
from download import teste_download
import pandas as pd
import csv
import folium
from geopy.geocoders import Nominatim
import pprint
import urllib.parse
import requests
import secrets
import itertools
from datetime import datetime
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


import secrets
secret_key = secrets.token_hex(16)
app.config['SECRET_KEY'] = secret_key

@app.route("/message", methods=['POST'])
def message():
  try:
    username = request.form.get('username')
    message = request.form.get('message')
    
  except Exception as e:
    print(e)
  return 'ok'


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
            #print(user_id)
            #print(file_to_save)
            fim = "Arquivo enviado com sucesso"
            error_ext ="Extensão inválida, envie arquivos .xlsx ou .csv"
            if not allow(file_to_save.filename):
                #print("EXTENSAO ERROR")
                return render_template('user_logged.html', fim=error_ext)
            else:
                salvar(user_id, file_to_save.filename, file_to_save)
                return render_template('user_logged.html', fim=fim)

@app.route("/analise_escolhido", methods=["POST"])
def download():
    user_uid = request.form['user_id_dois']
    file_name = request.form['filename']
    #print(user_uid + "_e_ " + file_name)
    #print('1   -------')
    try:
        results = []
        items= []
        df = teste_download(user_uid, file_name)
        #print(df)

        #---------- MANIPULAÇÂO

        df.drop(columns=range(4,24), inplace=True)
        df.drop(columns=[1,2], inplace=True)
        current_datetime = datetime.now()
        #print("11 ---concatenar")
        data_atual = str(current_datetime.day) +"-"+ str(current_datetime.month) +"-"+ str(current_datetime.year)
        df.rename(columns={
            0: 'nome',
            3:'data_nasc',
            'data_atual': 'data_atual'
        }, inplace=True)
        df['data_atual'] = data_atual
        df.data_nasc = df.data_nasc.replace('/','-', regex=True)
        df.drop(df.tail(1).index,inplace=True)
        df.data_nasc = df.data_nasc.fillna('01-01-1800')
        df.data_nasc = pd.to_datetime(df.data_nasc,format="%d-%m-%Y")
        df.data_atual = pd.to_datetime(df.data_atual,format="%d-%m-%Y")
        df.data_nasc = df.data_nasc.astype('string')
        df.data_atual = df.data_atual.astype('string')
        df[['ano_nasc', 'mes_nasc', 'dia_nasc']] = df.data_nasc.str.split('-', expand=True)
        df[['ano_atual', 'mes_atual', 'dia_atual']] = df.data_atual.str.split('-', expand=True)
        df['idade'] = df.ano_atual.astype(float) - df.ano_nasc.astype(float)

        df = df.loc[(df.dia_nasc==df.dia_atual) & (df.mes_nasc==df.mes_atual) ]
        #print("INDEX: ",df.index)
        lista_index = []
        for ind in df.index:
            lista_index.append(ind)
        tamanho_index = len(lista_index)
        #print('tamanho index: ', len(lista_index))
        #---------- MANIPULAÇÂO


        #print('error aqui')
        tamanho= int(df.shape[0])
        
        #print('1--------DICIONARIO------')
        
        dfdi= df.to_dict()

        for colum in dfdi.keys():
            results.append(colum) 


        for row in dfdi:
            items.append(dfdi[row])

        #print("TAMANHO ITems: ",tamanho)

        #print(results)
        #print('2--------Lista com os Results------')

        #print(df[results[1]])
        #print("Quantidade de linhas "+str(len(df[results[0]])))
        #print('3--------Teste------')

        quantidade_rows = df.shape[0]
        #print(df.shape[0])
        #print('4--------Teste  2------')
       #print(items)
        #print('5--------Teste  3------')
        #for row in items:
        #    #print(row)
            
            #for index in range(0,len(results)-1):
                
                #print(row[results[index]])
        '''#print(items[0][0])
        #print(items[1][0])
        #print(items[2][0])
        #print(items[3][0])
        #print(items[4][0])'''

        #print('6--------Teste  4------')
        #for row in items:
       #    # #print(row)
        #    for i in row:
             #   #print(row[i])
        """#print('7--------Teste 5------')
        #print(items[0])
        #print('8--------Teste6------')
        #print(items[0][0])
        #print('9--------Teste 8------')
        #print(items[6])
        #print('8--------Teste 9------')
        #print(items[6][0])"""


        return render_template('teste.html', results=results,items=items,tamanho=tamanho, quantidade_rows=quantidade_rows, df=df, len=len, uid=user_uid, file_name=file_name,lista_index=lista_index, tamanho_index=tamanho_index)
    except Exception as e:
        print(e)
        return "ERROR"

def pegarcoord():
    geolocator = Nominatim(user_agent="my_user_agent")
    rua='Largo Maria Martha Ward'
    city ="Rio de Janeiro"
    country ="Br"
    loc = geolocator.geocode(rua+','+city+','+ country)
    #print("latitude is :-" ,loc.latitude,"\nlongtitude is:-" ,loc.longitude)


@app.route("/gerargrafico", methods=['POST'])
def gerargrafico():
    user_uid = request.form['user_uid']
    file_name = request.form['filename']
    df = teste_download(user_uid, file_name)
    '''latitude = df['lat']
    longitude = df['long']'''
    endereco = df['Local da Concentraçao']
    #print(endereco[2])
    pegarcoord()
    #print("----------")

    return "ok"
    '''map = folium.Map(
        location=[latitude[0],longitude[0]],
        zoom_start=12
    )
    folium.Marker(
        
        location=[latitude, longitude],
        popup="<b>"+alerta+"!"+"<b>",
        icon=folium.Icon(
            color='red',
            icon='glyphicon glyphicon-warning-sign'
        ),
        tooltip="Clique Aqui!"
    ).add_to(map)'''
    

    '''return map._repr_html_()'''

@app.route("/visualizar")
def pag_visualizar():
    return render_template("visualizar.html")

@app.route("/criar")
def criar():
    return render_template("criar.html")


@app.route("/criar_tab", methods=['POST'])
def criar_tab():
    valor = request.form['valor']
    lista = []
    #print("VAlor :", valor)

    valor_a_somar = int(valor)
    valor_final = valor_a_somar+1
    #print(valor_final)
    try:
        for i in range(1,valor_final):
            nome = request.form[''+str(i)+'']
            lista.append(nome)
            #print(f"Loop nº {i} + Nome: {nome} ")

            i = i +1
    except Exception as e:
        print(e)
        
    #print(lista)
    return render_template('linhas.html', lista=lista)

@app.route("/criar_tab")
def redi():
    return render_template('linhas.html')
"""
@app.route("/<id>", methods=['POST'])
def testando(id):
    
    listinha  = request.form['listinha']
    nomes = []
    nome = listinha.split(",")
    nomes.append(nome)
    #print(id)
    #print(nomes)
    for item in nomes:
        for i in item:
            #print(i)
    return redirect(url_for('criar_tab'))"""

@app.route("/criar_dois")
def criar_dois():
    return render_template('criar_dois.html')

@app.route("/criar_dois_tab", methods=['POST'])
def criar_dois_tab():
    valor = request.form['valor']
    global lista_add
    lista = []
    #print("VAlor :", valor)

    valor_a_somar = int(valor)
    valor_final = valor_a_somar+1
    #print(valor_final)
    try:
        for i in range(1,valor_final):
            nome = request.form[''+str(i)+'']
            lista.append(nome)
            #print(f"Loop nº {i} + Nome: {nome} ")

            i = i +1
    except Exception as e:
        print(e)
        
    #print(lista)
    session['lista_add'] = lista
    return render_template('criar_dois_linhas.html', lista=lista)   

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(fillvalue=fillvalue, *args)

@app.route("/criar_novo_linhas", methods=['POST'])
def criar_novo_linhas():
    lista_pegar = session.get('lista_add')
    #print("Lista das Colunas :", lista_pegar)
    #print("Tamanho das colunas: ", len(lista_pegar))
    valor_a_resgatar = request.form['valor_a_resgatar']
    valor_a_resgatar_alterado = valor_a_resgatar.split(',')
    valores_finais = []
    for i in range(1, len(valor_a_resgatar_alterado)-1):
       valores_finais .append(valor_a_resgatar_alterado[i])
    #print("Linhas Resgatadas: ",valores_finais)
    
    tamanho_total = int(len(valores_finais))
    tamanho_dividido = int(len(valores_finais)/len(lista_pegar))
    
    #print("Tamanho total das linhas: ", tamanho_total)
    #print("Quantas linhas por colunas: ", tamanho_dividido)
 
    
    novo = list(grouper(int(tamanho_dividido), valores_finais))

    #print(novo)
    res = dict(zip(lista_pegar, novo))
    #print(res)

    #PEGAR COLUNAS
    try:
        results = []
        items= []
        for colum in res.keys():
            results.append(colum) 

        for row in res:
            items.append(res[row])


    except Exception as e:
        print(e)
    #TRANSFORMOU EM DATAFRAME FINAL
    new = pd.DataFrame.from_dict(res)
    #print(new)
    return render_template('last.html', results=results, items=items, len=len)

@app.route("/pag_chat")
def pag_chat():
    return render_template('pag_chat.html')

if __name__ == "__main__":
    app.run(debug=True, port=port)