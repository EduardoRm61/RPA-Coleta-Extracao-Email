import requests
import sqlite3
import sys
import io

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
email = 'eduardonunesdasilva23@gmail.com'


def criaBanco(info01, info02, info03, info04):
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

