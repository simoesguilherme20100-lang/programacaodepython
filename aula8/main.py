


import tkinter as tk 
import matplotlib.pyplot as plt
import pandas as pd


def mostrar():
    dados  =  {
        'vendas' : [1000,3000,6000],
        'meses':['jan', 'fev', 'mar']
               
        
    }
    
    df  =  pd.DataFrame(dados)
    medida_tend =  df.describe()
    texto.config(text= medida_tend)
    plt.bar(df['meses'], df['vendas'])
    plt.show()
    
    
    


janela  =  tk.Tk()
janela.geometry('300x300')


# widget 
# botões  -  inputs  -  textos -  links


texto_t =  tk.Label(janela, text = 'ANALISE DE DADOS', font= ('arial', 15))
texto_t.pack()




btn = tk.Button(janela, text='grafico barras', command=mostrar)
btn.pack(pady=10)


texto =  tk.Label(janela, text = '')
texto.pack()


janela.mainloop()