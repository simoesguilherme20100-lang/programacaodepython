

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# carregamento  
dados =  pd.read_csv('vendas.csv')

df =  pd.DataFrame(dados)
df['Data'] = pd.to_datetime(df['Data']) # tratamos a data 
df['Faturamento'] = df['Quantidade'] * df['Preco']

# print(df.tail)

# indicares 

faturamento_total =  df['Faturamento'].sum() 
quantidade_total = df['Quantidade'].sum()
ticket_medio = df['Faturamento'].mean()

# plt.figure(figsize=(6,6))
# plt.bar(df['Faturamento'], df['Produto'])
# plt.show()

print('Indicadores: ')
print('Faturamento Total', float(faturamento_total))

# analise por produto 


produtos = (
    df.groupby('Produto')
    .agg(
        Quantidade = ('Quantidade', 'sum'),
        Faturamento = ('Faturamento', 'sum')
        
    ).sort_values('Faturamento', ascending=True)

)
print('Analise por produto: ')
print(produtos)

# produto mais vendido 

produto_mais_vendido =  (df.groupby("Produto")["Quantidade"].sum()
                         .sort_values(ascending=True))           



print('Produto mais vendido')
print(produto_mais_vendido)

produto_maior_faturamento  =  (df.groupby("Produto")['Faturamento']
                               .sum().sort_values(ascending=True))
print('Produto com maior faturamento')
print(produto_maior_faturamento)



