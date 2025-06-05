import requests
import sqlite3
import sys
import io
import json

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
email = 'eduardonunesdasilva23@gmail.com'

url = 'https://api.thecatapi.com/v1/breeds'

def criaBanco(raca, origem, cod_pais, temp, peso, pag):
    pass

def extraiDados(url_base):
    #url_base = requests.get(url_base)
    resposta = requests.get(url_base)

    if resposta.status_code!=200:
        print({"Erro:":"Não foi possível buscar os dados"})
        return
    
    dados = resposta.json()
    if not dados:
        print({"Erro":"Não foi possível buscar as informações"})

    api = dados[0]
    try:
        for api in dados:
            raca = api.get('name', 'Desconhecido')
            origem = api.get('origin', 'Desconhecido')
            cod_pais = api.get('country_code', 'N/A')
            temp = api.get('temperament', 'N/A')
            peso = api.get('weight', {}).get('imperial', 'N/A')
            pag = api.get('wikipedia_url', 'Sem Link') 
            criaBanco(raca, origem, cod_pais, temp, peso, pag)

    except Exception as e:
        print({"Erro ao processar dados": str(e)})





def enviaEmail(email):
    try:
        print("Estamos preparando seu e-mail... ⏳")

        servidor_email = smtplib.SMTP('smtp.gmail.com', 587)
        servidor_email.starttls()
        servidor_email.login(email,'rphn ilwo ihtf iweb')

        remetente = email
        destinatario = ['eduardo.nsilva@aluno.faculdadeimpacta.com.br']

        mensagem = MIMEMultipart()
        mensagem['From'] = remetente
        mensagem['To'] = ", ".join(destinatario)
        mensagem['Subject'] = "Email Teste"

        corpo = "Olá, este e-mail foi enviado para informar que todo o processo acorreu com êxito!"
        mensagem.attach(MIMEText(corpo,'plain'))

        servidor_email.sendmail(remetente, destinatario, mensagem.as_string())

        print(f"E-mail enviado para '{email}' com êxito!!")

    except Exception as e:
        print(f"Erro, não foi possível enviar o e-mail: {e}")




#print(dados)

# 1 - Pegando o nome da Raça
# for name in dados:
#     raca = name['name']
#     print(raca)

# 2 - Pegando a origem dela
# for origin in dados:
#     name = origin['origin']
#     print(name)

# 3 - Capturando código do país:
# for code in dados:
#     name = code['country_code']
#     print(name)

# 4 - Capturando o temperamento
# for temp in dados:
#     name = temp['temperament']
#     print(name)

# 5 - Capturando o peso
# for peso in dados:
#     weight = peso['weight']['imperial']
#     print(weight)

# 6 - Capturando página na Wiki
# for pag in dados:
#     name = pag.get('wikipedia_url', "Sem Link")
#     print(name)
