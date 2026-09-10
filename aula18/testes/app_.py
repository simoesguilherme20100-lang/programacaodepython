
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestClassifier 
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk

# ml

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder


url = 'https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv'
df =  pd.read_csv(url)

# DADOS 

# df['Age'].fillna(df['Age'].median(), inplace=True)
# df['Sex'] = LabelEncoder().fit_transform(df['Sex'])
# df['Pclass'] = df['Pclass'].astype('category')



# interface grafica 

root = tk.Tk()
root.title('Analise titanic')
root.geometry('2000x1700')

frame_grafico = tk.Frame(root)
frame_grafico.pack(pady=20, fill=tk.BOTH, expand=True)

frame_controle  =  tk.Frame(root)
frame_controle.pack(pady=10)

frame_resultados =  tk.Frame(root)
frame_resultados.pack(pady = 10)

label_tendencia =  tk.Label(frame_resultados, text='', justify=tk.LEFT)
label_tendencia.pack()

label_descricao = tk.Label(frame_resultados, text='', justify=tk.LEFT)
label_descricao.pack()

label_previsao = tk.Label(frame_resultados, text='', justify=tk.LEFT)
label_previsao.pack()

# ------------------------------- 

# funções de analise ... 

def limpar_frame():
    for widget in frame_grafico.winfo_children():
        widget.destroy()
        
        
        
        
        

        
# --------------------------------------------        
# botões 

btn_barras  = ttk.Button(frame_controle, text= 'Grafico de barras')
btn_barras.grid(row = 0, padx= 5, pady=5)

btn_linhas  = ttk.Button(frame_controle, text= 'Grafico de linhas')
btn_linhas.grid(row = 1, padx= 5, pady=5)

btn_pizza  = ttk.Button(frame_controle, text= 'Grafico de Pizza')
btn_pizza.grid(row = 2, padx= 5, pady=5)

btn_tendecia  = ttk.Button(frame_controle, text= 'Medida de tendência')
btn_tendecia.grid(row = 3, padx= 5, pady=5)

btn_descricao = ttk.Button(frame_controle, text= 'Descrição')
btn_descricao.grid(row = 4, padx= 5, pady=5)

btn_previsao  = ttk.Button(frame_controle, text= 'Previsão')
btn_previsao.grid(row = 5, padx= 5, pady=5)



        

















root.mainloop()


