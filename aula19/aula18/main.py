
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

frame_resultados =  tk.Frame(root)
frame_resultados.pack(pady = 10)

frame_controle  =  tk.Frame(root)
frame_controle.pack(pady=10)

label_tendencia =  tk.Label(frame_resultados, text='', justify=tk.CENTER)
label_tendencia.pack()

label_descricao = tk.Label(frame_resultados, text='', justify=tk.LEFT)
label_descricao.pack()

label_previsao = tk.Label(frame_resultados, text='', justify=tk.LEFT)
label_previsao.pack()

# ------------------------------- 



# limpando 
def limpar_frame():
    for widget in frame_grafico.winfo_children():
        widget.destroy()




# funções de analise ...         
        
def mostrar_barras():
    limpar_frame()
    fig, ax =  plt.subplots(figsize = (8,5))
    sobreviventes_por_classe = df.groupby('Pclass')['Survived'].mean() * 100
    sobreviventes_por_classe.plot(kind='bar', color = ['blue','green','yellow'], ax=ax)  
     
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, expand=True)
    
    ax.set_title('SOBREVIVENTES POR CLASSE')
    ax.set_ylabel('Porcentagem ')
    ax.set_xlabel('Classe dos Sobreviventes')
    
    insight =  'Passageiros da 1º Classe tiveram maior taxa de sobrevivência'        
    label_tendencia.config(text= insight, )      

def mostrar_linhas():
    limpar_frame()
    fig, ax =  plt.subplots(figsize = (8,5))
    idade_media_sobreviventes   =   df[df['Survived'] == 1].groupby('Pclass')['Age'].mean()
    idade_media_naosobreviventes = df[df['Survived'] == 0].groupby('Pclass')['Age'].mean()   
    idade_media_sobreviventes.plot(kind  = 'line', color = 'blue', ax=ax)
    idade_media_naosobreviventes.plot(kind  = 'line', color = 'red',ax=ax)
    
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, expand=True)
    
    ax.set_title('SOBREVIVENTES POR IDADE')
    ax.set_ylabel('MÉDIA')
    ax.set_xlabel('CLASSE')
    ax.legend(labels = ['Não sobreviveu', 'Sobreviveu'])
    
    insight =  'Passageiros mais jovens da 3º classe tiveram menor chances de sobrevivência'        
    label_tendencia.config(text= insight)      
     
     
def mostrar_pizza():
    limpar_frame()
    fig, ax =  plt.subplots(figsize = (8,5))
    sobreviventes  = df['Survived'].value_counts()
    sobreviventes.plot(kind = 'pie', autopct = '%1.1f%%', labels = ['Não sobreviveu', 'Sobreviveu'])    
    
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, expand=True)
    
    ax.set_title('DISTRIBUIÇÃO DOS SOBREVIVENTES')
    
    
    insight =  'Apenas 38% dos passageiros sobreviveu'        
    label_tendencia.config(text= insight)     
    
def mostrar_tendencia():
    limpar_frame()
    # fig, ax =  plt.subplots(figsize = (8,5))
    
    idade_media  =  df['Age'].mean()
    idade_mediana  =  df['Age'].median()
    idade_moda =  df['Age'].mode()[0]
    
    tarifa_media  =  df['Fare'].mean()
    tarifa_medianan  =  df['Fare'].median()
    tarifa_moda  =  df['Fare'].mode()[0]
    
    resultado = (
        f'IDADE'
        
        f'Media de idade - {idade_media}\n'
        f'Mediana - {idade_mediana}\n'
        f'Moda - {idade_moda}\n'
        
        
        f'TARIFA'
        
        f'Tarida Media - {tarifa_media} \n'
        f'Tarifa Mediana - {tarifa_medianan}\n'
        f'Tarifa Moda {tarifa_moda}\n'  ) 
           
    # canvas = FigureCanvasTkAgg(fig, master=frame_resultados)
    # canvas.draw()
    # canvas.get_tk_widget().pack(side=tk.TOP, expand=True)   
    
    insight =  'A mediana da tarifa é menor que a média, deduz que poucos passageiros pagaram tarifas altas'         
    label_tendencia.config(text= resultado + '\n' + insight)  
    
def descricao():
    descricao  = df[["Age", "Fare", "Pclass", "Survived"]].describe().to_string() 
    
    insight = '75% dos passageiros pagaram até l$ 31.00 mas o máximo era l$ 512.33'
    
    label_descricao.config(text = descricao +  '\n' + insight) 
    
def previsao():
    
    features =  ['Pclass', 'Sex', 'Age','Fare']
    X = df[features]
    y = df['Survived']
    
    X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=42, test_size=0.2)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred  = model.predict(X_test) # y  =  f(x)
        
    importancia  =  pd.Series(model.feature_importances_, index=features).sort_values(ascending=False) 
    
    acuracia = accuracy_score(y_test, y_pred)
    
    fig, ax =  plt.subplots(figsize = (8,5))
    importancia.plot(kind='bar', ax= ax)
    
    ax.set_title('Caracteristicas da previsão')

    canvas = FigureCanvasTkAgg(fig, master=frame_resultados)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, expand=True) 
    
     
    insight = 'As pesssoas com mais chance de sobrevivência são pessoas do sexo feminino'
    
    resultado =  (
        
        f' acuracia  - {acuracia * 100} \n'
        f'1 -  Sexo Feminino - 0 | Sexo Masculino - 1  \n'
        f'2 -  Classe \n'
        f'3 -  Idade\n'
        f'4 -  Tarifa\n'
        
    )
    
    label_previsao.config(text= resultado + '\n '+  insight)    
              
     
# --------------------------------------------        
# botões 

btn_barras  = ttk.Button(frame_controle, text= 'Grafico de barras', command=mostrar_barras)
btn_barras.grid(row = 0, padx= 5, pady=5)

btn_linhas  = ttk.Button(frame_controle, text= 'Grafico de linhas', command=mostrar_linhas)
btn_linhas.grid(row = 1, padx= 5, pady=5)

btn_pizza  = ttk.Button(frame_controle, text= 'Grafico de Pizza', command= mostrar_pizza)
btn_pizza.grid(row = 2, padx= 5, pady=5)

btn_tendecia  = ttk.Button(frame_controle, text= 'Medida de tendência', command=mostrar_tendencia)
btn_tendecia.grid(row = 3, padx= 5, pady=5)

btn_descricao = ttk.Button(frame_controle, text= 'Descrição', command=descricao)
btn_descricao.grid(row = 4, padx= 5, pady=5)

btn_previsao  = ttk.Button(frame_controle, text= 'Previsão', command=previsao)
btn_previsao.grid(row = 5, padx= 5, pady=5)



        

















root.mainloop()

