


import tkinter as tk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt

# Conectar ao banco de dados
conexao = sqlite3.connect('meu_banco_de_dados.db')
cursor = conexao.cursor()

# Criar a tabela se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        cidade TEXT NOT NULL
    )
''')
conexao.commit()


# Função para inserir os dados no banco de dados
def inserir_pessoa():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    cidade = entrada_cidade.get()

    if nome == "" or idade == "" or cidade == "":
        messagebox.showwarning(
            "Atenção",
            "Preencha todos os campos."
        )
        return

    try:
        idade = int(idade)

        cursor.execute('''
            INSERT INTO pessoas (nome, idade, cidade)
            VALUES (?, ?, ?)
        ''', (nome, idade, cidade))

        conexao.commit()

        messagebox.showinfo(
            "Sucesso",
            "Pessoa cadastrada com sucesso!"
        )

        entrada_nome.delete(0, tk.END)
        entrada_idade.delete(0, tk.END)
        entrada_cidade.delete(0, tk.END)

    except ValueError:
        messagebox.showerror(
            "Erro",
            "A idade deve ser um número inteiro."
        )


# Criar janela
janela = tk.Tk()
janela.title("Cadastro de Pessoas")
janela.geometry("400x300")


# Nome
tk.Label(janela, text="Nome:").pack(pady=5)
entrada_nome = tk.Entry(janela, width=40)
entrada_nome.pack()


# Idade
tk.Label(janela, text="Idade:").pack(pady=5)
entrada_idade = tk.Entry(janela, width=40)
entrada_idade.pack()


# Cidade
tk.Label(janela, text="Cidade:").pack(pady=5)
entrada_cidade = tk.Entry(janela, width=40)
entrada_cidade.pack()


# Botão cadastrar
botao = tk.Button(
    janela,
    text="Cadastrar",
    command=inserir_pessoa
)
botao.pack(pady=20)


# Iniciar aplicação
janela.mainloop()


# Fechar conexão com o banco
conexao.close()