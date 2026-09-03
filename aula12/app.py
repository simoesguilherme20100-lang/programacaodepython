


import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st



dados =  sns.load_dataset('titanic')
df =  pd.DataFrame(dados)
st.header('Analise de dados')
# # print(dados)


sns.barplot(x = dados['sex'], y = dados['age'], data = dados)
# plt.title('Genero dentro do Titanic')
# plt.show()
st.write(dados)
st.bar_chart(df, x= 'sex', y  = 'age')
st.map()

