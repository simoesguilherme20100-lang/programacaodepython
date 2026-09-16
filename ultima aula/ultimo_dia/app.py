
import streamlit as st
import sqlite3 
import plotly.express as px 
import pandas as pd

st.header('ANALISE')

conn =  sqlite3.connect('vendas_prod.db')
cursor =  conn.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS vendas(
       
    produto TEXT,
    valor REAL,
    quantidade INTEGER
       
    
) ''')


# produto =  st.text_input('Digite o produto: ')
produto =  st.text_input('Produto: ')
valor  =  st.number_input('Valor', value = 0)
# n_v =  valor.replace('.','')

quantidade  =  st.number_input('Quantidade')

st.markdown('***')


# cursor.execute('SELECT COUNT(*) FROM vendas')
if st.button('Inserir'):
    cursor.execute('INSERT INTO vendas VALUES(?,?,?)', (produto, n_v, quantidade))
    conn.commit()



# leitura dos dados
df  =  pd.read_sql_query('SELECT * FROM  vendas', conn)
conn.close()

# st.write(df)

st.table(df)


st.markdown('***')

st.subheader('Resumo dos dados')
total_faturamento  = (df['valor'] * df['quantidade']).sum()

st.write('Faturamento total', f' R$ {total_faturamento}')
st.subheader('GRAFICO DE BARRAS')
fig = px.bar(df, x =  'produto', y= 'valor', title='VALOR PRODUTO')

st.plotly_chart(fig, use_container_width=True)

st.markdown('***')

st.subheader('produtos: ')

left, middle, right = st.columns(3)

left.image('a.png')
middle.image('b.png')
right.image('c.png')

fig = px.pie(df, values= df['quantidade'], names=df['produto'])

st.plotly_chart(fig, use_container_width=True)