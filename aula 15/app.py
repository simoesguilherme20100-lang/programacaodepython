

import sqlite3
import pandas as pd

# esta criando o arquivo sql db -> database 
banco =  sqlite3.connect('dados.db')

# para digitar sql no arquivo python
# cursor do banco
cursor =  banco.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS clientes(
                 
                 id INTEGER PRIMARY  KEY AUTOINCREMENT,
                 nome TEXT NOT NULL,
                 email TEXT NOT NULL,
                 salario REAL NOT NULL,
                 cargo  TEXT NOT  NULL
     
)''') 

banco.commit()
# banco.close()


# CREATE - CRIA A TABELA
# INSERT -  INSERIR DADOS NA TABELA

cursor.execute('INSERT INTO clientes (nome,email,salario,cargo) VALUES(?, ?, ?, ?)', ('Ana','ana@gmail.com',4500.0,'Analista'))
banco.commit()               
               
cursor.execute('INSERT INTO clientes (nome,email,salario,cargo) VALUES(?, ?, ?,?)', ('Kaio','kaka@gmail.com',3500.0,'Estagiário'))
banco.commit()     

cursor.execute('INSERT INTO clientes  (nome,email,salario,cargo) VALUES(?, ?, ?, ?)', ('Felipe','fe@gmail.com',1500.0,'Menor Ap.'))
banco.commit()      

cursor.execute('INSERT INTO clientes  (nome,email,salario,cargo) VALUES(?, ?, ?, ?)', ('Bernardo','ber@gmail.com',9500.0,'Coordenador'))
banco.commit()     

cursor.execute('SELECT * FROM clientes')
DADOS_ = cursor.fetchall()

df  =  pd.DataFrame(DADOS_)
df.to_csv('clientes.csv', index=False)

df = df.rename(columns={
    
    0:'id',
    1:'nome',
    2:'email',
    3:'salario',
    4:'cargo'
    
    })


print(df)


# for n in DADOS_:
#     # print(n)



# SELECIONAR COLUNAS:


cursor.execute('SELECT  nome, salario FROM clientes')
dados_  = cursor.fetchall()

# for n in dados_:
#     print(n)


# print(DADOS_)
