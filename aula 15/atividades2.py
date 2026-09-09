


import tkinter as tk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt


# BANCO DE DADOS


conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER NOT NULL,
    genero TEXT NOT NULL,
    paginas INTEGER NOT NULL
)
""")

conexao.commit()



# CADASTRAR LIVRO


def cadastrar():
    titulo = entrada_titulo.get()
    autor = entrada_autor.get()
    ano = entrada_ano.get()
    genero = entrada_genero.get()
    paginas = entrada_paginas.get()

    if titulo == "" or autor == "" or ano == "" or genero == "" or paginas == "":
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return

    try:
        ano = int(ano)
        paginas = int(paginas)

        cursor.execute("""
        INSERT INTO livros (titulo, autor, ano, genero, paginas)
        VALUES (?, ?, ?, ?, ?)
        """, (titulo, autor, ano, genero, paginas))

        conexao.commit()

        messagebox.showinfo("Sucesso", "Livro cadastrado!")

        entrada_titulo.delete(0, tk.END)
        entrada_autor.delete(0, tk.END)
        entrada_ano.delete(0, tk.END)
        entrada_genero.delete(0, tk.END)
        entrada_paginas.delete(0, tk.END)

        atualizar_lista()

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Ano e páginas devem ser números!"
        )



# ATUALIZAR LISTA


def atualizar_lista():

    lista.delete(0, tk.END)

    cursor.execute("""
    SELECT * FROM livros
    ORDER BY id
    """)

    livros = cursor.fetchall()

    for livro in livros:
        lista.insert(
            tk.END,
            f"ID: {livro[0]} | "
            f"Título: {livro[1]} | "
            f"Autor: {livro[2]} | "
            f"Ano: {livro[3]} | "
            f"Gênero: {livro[4]} | "
            f"Páginas: {livro[5]}"
        )



# LIVROS POR ANO


def livros_por_ano():

    cursor.execute("""
    SELECT ano, COUNT(*)
    FROM livros
    GROUP BY ano
    ORDER BY ano
    """)

    dados = cursor.fetchall()

    if not dados:
        messagebox.showinfo("Aviso", "Nenhum livro cadastrado.")
        return

    anos = [str(x[0]) for x in dados]
    quantidades = [x[1] for x in dados]

    plt.bar(anos, quantidades)

    plt.title("Livros por Ano")
    plt.xlabel("Ano")
    plt.ylabel("Quantidade de Livros")

    plt.show()



# LIVROS POR GÊNERO


def livros_por_genero():

    cursor.execute("""
    SELECT genero, COUNT(*)
    FROM livros
    GROUP BY genero
    """)

    dados = cursor.fetchall()

    if not dados:
        messagebox.showinfo("Aviso", "Nenhum livro cadastrado.")
        return

    generos = [x[0] for x in dados]
    quantidades = [x[1] for x in dados]

    plt.bar(generos, quantidades)

    plt.title("Livros por Gênero")
    plt.xlabel("Gênero")
    plt.ylabel("Quantidade")

    plt.xticks(rotation=30)

    plt.show()



# PÁGINAS POR GÊNERO


def paginas_por_genero():

    cursor.execute("""
    SELECT genero, SUM(paginas)
    FROM livros
    GROUP BY genero
    """)

    dados = cursor.fetchall()

    if not dados:
        messagebox.showinfo("Aviso", "Nenhum livro cadastrado.")
        return

    generos = [x[0] for x in dados]
    paginas = [x[1] for x in dados]

    plt.bar(generos, paginas)

    plt.title("Páginas por Gênero")
    plt.xlabel("Gênero")
    plt.ylabel("Total de Páginas")

    plt.xticks(rotation=30)

    plt.show()



# ESTATÍSTICA GERAL


def estatistica_geral():

    cursor.execute("""
    SELECT
        COUNT(*),
        SUM(paginas),
        AVG(paginas),
        MIN(paginas),
        MAX(paginas)
    FROM livros
    """)

    dados = cursor.fetchone()

    total_livros = dados[0]

    if total_livros == 0:
        messagebox.showinfo(
            "Estatística",
            "Nenhum livro cadastrado."
        )
        return

    total_paginas = dados[1]
    media = dados[2]
    menor = dados[3]
    maior = dados[4]

    cursor.execute("""
    SELECT genero, COUNT(*)
    FROM livros
    GROUP BY genero
    ORDER BY COUNT(*) DESC
    LIMIT 1
    """)

    genero = cursor.fetchone()[0]

    texto = (
        "ESTATÍSTICA GERAL\n\n"
        f"Total de livros: {total_livros}\n"
        f"Total de páginas: {total_paginas}\n"
        f"Média de páginas: {media:.2f}\n"
        f"Menor número de páginas: {menor}\n"
        f"Maior número de páginas: {maior}\n"
        f"Gênero com mais livros: {genero}"
    )

    messagebox.showinfo(
        "Estatística Geral",
        texto
    )



# JANELA


janela = tk.Tk()
janela.title("Sistema de Biblioteca")
janela.geometry("900x650")


# Título
tk.Label(
    janela,
    text="SISTEMA DE BIBLIOTECA",
    font=("Arial", 20, "bold")
).pack(pady=15)



# CAMPOS


frame = tk.Frame(janela)
frame.pack()


tk.Label(frame, text="Título:").grid(
    row=0, column=0, padx=5, pady=5
)

entrada_titulo = tk.Entry(frame, width=40)
entrada_titulo.grid(row=0, column=1)


tk.Label(frame, text="Autor:").grid(
    row=1, column=0, padx=5, pady=5
)

entrada_autor = tk.Entry(frame, width=40)
entrada_autor.grid(row=1, column=1)


tk.Label(frame, text="Ano:").grid(
    row=2, column=0, padx=5, pady=5
)

entrada_ano = tk.Entry(frame, width=40)
entrada_ano.grid(row=2, column=1)


tk.Label(frame, text="Gênero:").grid(
    row=3, column=0, padx=5, pady=5
)

entrada_genero = tk.Entry(frame, width=40)
entrada_genero.grid(row=3, column=1)


tk.Label(frame, text="Páginas:").grid(
    row=4, column=0, padx=5, pady=5
)

entrada_paginas = tk.Entry(frame, width=40)
entrada_paginas.grid(row=4, column=1)



# BOTÃO CADASTRAR


tk.Button(
    janela,
    text="CADASTRAR LIVRO",
    command=cadastrar,
    width=25
).pack(pady=15)



# LISTA


tk.Label(
    janela,
    text="LIVROS CADASTRADOS",
    font=("Arial", 12, "bold")
).pack()

lista = tk.Listbox(
    janela,
    width=120,
    height=10
)

lista.pack(pady=10)



# BOTÕES DE ANÁLISE


frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)


tk.Button(
    frame_botoes,
    text="LIVROS POR ANO",
    command=livros_por_ano,
    width=20
).grid(row=0, column=0, padx=5, pady=5)


tk.Button(
    frame_botoes,
    text="LIVROS POR GÊNERO",
    command=livros_por_genero,
    width=20
).grid(row=0, column=1, padx=5, pady=5)


tk.Button(
    frame_botoes,
    text="PÁGINAS POR GÊNERO",
    command=paginas_por_genero,
    width=20
).grid(row=0, column=2, padx=5, pady=5)


tk.Button(
    frame_botoes,
    text="ESTATÍSTICA GERAL",
    command=estatistica_geral,
    width=20
).grid(row=1, column=0, padx=5, pady=5)


tk.Button(
    frame_botoes,
    text="ATUALIZAR LISTA",
    command=atualizar_lista,
    width=20
).grid(row=1, column=1, padx=5, pady=5)


# Atualizar lista ao iniciar
atualizar_lista()


# Iniciar programa
janela.mainloop()


# Fechar banco
conexao.close()