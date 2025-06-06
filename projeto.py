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

def guardaBanco(raca, origem, cod_pais, temp, peso, pag,cursor):
    cursor.execute('''
        INSERT INTO Gatos(
                   raca, origem, cod_pais, 
                   temperamento, peso, pagina_Wiki
                   ) VALUES (?,?,?,?,?,?)
                ''',(
                    raca, origem, cod_pais,
                    temp, peso, pag
                ))

    
    
def filters():
    conexao = sqlite3.connect('projeto_rpa.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Gatos_Resumo(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   raca TEXT,
                   origem TEXT,
                   pagina_Wiki TEXT
                )
            ''')
    
    #cursor.execute('DELETE FROM Gatos_Resumo')
    
    cursor.execute('''
         SELECT raca, origem, pagina_wiki FROM Gatos
''')
    dados_filtrados = cursor.fetchall()

    for linha in dados_filtrados:
        cursor.execute('''
            INSERT INTO Gatos_Resumo (raca, origem, pagina_Wiki)
            VALUES (?, ?, ?)
        ''', linha)

    conexao.commit()
    conexao.close()

def extraiDados(url_base):
    #url_base = requests.get(url_base)
    resposta = requests.get(url_base)

    if resposta.status_code!=200:
        print({"Erro:":"Não foi possível buscar os dados"})
        return
    
    dados = resposta.json()
    if not dados:
        print({"Erro":"Não foi possível buscar as informações"})

    
    conexao = sqlite3.connect('projeto_rpa.db')
    cursor = conexao.cursor()


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Gatos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            raca TEXT,
            origem TEXT,
            cod_pais TEXT,
            temperamento TEXT,
            peso TEXT,
            pagina_Wiki TEXT
        )
    ''')

    try:
        for api in dados:
            raca = api.get('name', 'Desconhecido')
            origem = api.get('origin', 'Desconhecido')
            cod_pais = api.get('country_code', 'N/A')
            temp = api.get('temperament', 'N/A')
            peso = api.get('weight', {}).get('imperial', 'N/A')
            pag = api.get('wikipedia_url', 'Sem Link') 

            guardaBanco(raca, origem, cod_pais, temp, peso, pag, cursor)

        conexao.commit()
        conexao.close()
        filters()

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


extraiDados(url)
enviaEmail(email)

conexao = sqlite3.connect('projeto_rpa.db')
cursor = conexao.cursor()

print("\n Conteúdo da tabela Gatos:")
cursor.execute('SELECT * FROM Gatos')
for linha in cursor.fetchall():
    print(linha)

print("\nConteúdo da tabela Gatos_Resumo:")
cursor.execute('SELECT * FROM Gatos_Resumo')
for linha in cursor.fetchall():
    print(linha)