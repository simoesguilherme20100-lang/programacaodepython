import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


url = "https://bea3853.github.io/PROCESSO_DATA_SCIENCE/"
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


# Salvando em CSV (opcional)
df.to_csv('smartphones.csv', index=False)

#### 2. Limpeza e Análise Exploratória (Pandas + NumPy)  

# Carregar dados (se não vier do scraping)
df = pd.read_csv('smartphones.csv')

# Verificar dados faltantes
print(df.isnull().sum())

# Limpeza: Remover duplicatas e outliers
df = df.drop_duplicates()
df = df[df['Preco'] < 10000]  # Filtrar preços absurdos

# Extrair marca do modelo (ex.: "iPhone 15" -> "Apple")
df['Marca'] = df['Modelo'].str.split().str[0]

# Estatísticas básicas
print(df.describe())

# Preço médio por marca
preco_medio = df.groupby('Marca')['Preco'].mean().sort_values(ascending=False)
print(preco_medio)