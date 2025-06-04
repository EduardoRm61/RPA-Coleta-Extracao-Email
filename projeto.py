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

def criaBanco(info01, info02, info03, info04):
    pass

def extraiDados(url_base):
    pass

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

resposta = requests.get(url)
dados = resposta.json()
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
for peso in dados:
    weight = peso['weight']['imperial']
    print(weight)