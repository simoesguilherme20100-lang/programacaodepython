import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


url = "https://bea3853.github.io/PROCESSO_DATA_SCIENCE/"
# url = "https://bea3853.github.io/site-ecommerce/"
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

nomes = []
precos = []
avaliacoes = []


for produto in soup.find_all('div', class_='produto'):
    nomes.append(produto.find('h2').text)
    precos.append(float(produto.find('span', class_='preco').text.replace('R$', '').replace('.', '').replace(',', '.')))
    avaliacoes.append(float(produto.find('span', class_='avaliacao').text))


df = pd.DataFrame({
    'Modelo': nomes,
    'Preco': precos,
    'Avaliacao': avaliacoes
})


print('DATA FRAME', df)

# Salvando em CSV (opcional)
df.to_csv('smartphones.csv', index=False)
# df.to_html('index2.html')
# df.to_excel('dados.xlsx')

#### 2. Limpeza e Análise Exploratória (Pandas + NumPy)  

# Carregar dados (se não vier do scraping)
df = pd.read_csv('smartphones.csv')

# Verificar dados faltantes
df.isnull().sum()

print('***  ' * 10)

# Limpeza: Remover duplicatas e outliers
df = df.drop_duplicates()

precos_ =  df = df[df['Preco'] < 10000]

print('*** ' * 10)


print(precos_)  # Filtrar preços absurdos

# Extrair marca do modelo (ex.: "iPhone 15" -> "Apple")

marca = df['Marca'] = df['Modelo'].str.split().str[0]
print('MARCA DO MODELO', marca)

print('*** ' * 10)


# Estatísticas básicas
print('ESTATISTICA:', df.describe())


print('*** ' * 10)

# Preço médio por marca
preco_medio = df.groupby('Marca')['Preco'].mean().sort_values(ascending=False)
print('PRECO MÉDIO', preco_medio)


# GRAFICOS 

plt.figure(figsize=(10,6))
plt.hist(df['Preco'], bins=20, color='blue', edgecolor = 'black')
plt.title('DISTRIBIUÇÃO DOS PREÇOS DOS SMARTFONES')
plt.ylabel('Preço R$')
plt.xlabel('Quantidade')
plt.grid(True)
plt.show()


plt.figure(figsize=(10,6))
preco_medio.plot(kind = 'bar', color = 'orange')
plt.title('PREÇO MÉDIO POR MARCA')
plt.ylabel('Marca ')
plt.xlabel('Preço')
plt.grid(axis = 'y')
plt.tick_params("x", rotation= 50 )
plt.show()


# relação de preço x avaliação

plt.figure(figsize=(10,6))
plt.scatter(df['Preco'], df['Avaliacao'],alpha=0.6, color = 'green')
plt.title('RELAÇÃO DE PREÇO X AVALIAÇÃO')
plt.ylabel('AVALIAÇÃO')
plt.xlabel('Preço')
plt.grid(axis = 'y')
# plt.tick_params("x", rotation= 50 )
plt.show()
