import matplotlib.pyplot as plt
import pandas as pd 



fig, ax  =  plt.subplots()
 


dados =  pd.read_csv('dados.csv')
plt.title('Isso  é um titulo')


ax.bar(dados['nome'], dados['idade'])
ax.set_xlabel('eixo X')
ax.set_ylabel('eixo Y')


plt.show() 