

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

# hipoteses

produto_volume  =  produto_mais_vendido.index[0]
produto_receita = produto_maior_faturamento.index[0]

print(produto_volume)
print(produto_receita)

print(f'''
      
      O produto {produto_volume} possui o maior volume de vendas
      O produto {produto_receita} possui a maior receita e gera 
      mais faturamento.
            
      ''')

print(f'''
      
      O produto de maior venda - {produto_volume}  pode gerar mais receita 
      mesmo apresentando menor quantidade de vendas.
       
      
      ''')

print(f'''
       
       Decisão:
       investigar estratégias para aumentar o volume de vendas,
       de {produto_receita}, sem reduzir signitificatimente, sua margem o volume
           
      ''')


# analise de produtos alto volume de vendas e baixo faturamento

media_quantidade  =  produtos['Quantidade'].mean()
media_faturamento =  produtos['Faturamento'].mean()

produtos_alto_volume = produtos[
                       (produtos['Quantidade'] > media_quantidade) &
                       (produtos['Faturamento']< media_faturamento)
       
]

print('produtos com alto volume de vendas e baixo faturamento')                                
print(produtos_alto_volume)

# hipoteses sobre os dados dos baixo faturamento e alto volume 


print('''
      
       Produtos com grande volume de vendas e menor faturamento,
       podem ser utilizados como produtos de entrada.
      
      
      ''')
                                                                
print('''
      Decisão:
      
      Criar estratégias de venda combinada com produtos de 
      maior valor agregado. 
      
      
      ''')

print('Monitos + teclado + mouse')


# ANALISE POR CIDADES:


cidades = (
    df.groupby('Cidade')
    .agg(
        Quantidade = ('Quantidade', 'sum'),
        Faturamento = ('Faturamento', 'sum')
        
    ).sort_values('Faturamento', ascending=True)    
    )                      

print(cidades)



# Ticket médio 

ticket_cidade  =   (df.groupby("Cidade")['Faturamento']
                               .mean().sort_values(ascending=True)
                   )

print('Ticket médio por cidade::')
print(ticket_cidade)


# hipotese geografica
print()
print('ANALISE GEOGRAFICA')

cidade_maior_faturamento  =  cidades['Faturamento'].idxmax()
cidade_menor_faturamento  = cidades['Faturamento'].idxmin()


print(f'''
      
      a cidade com maior faturamento é  =  {cidade_maior_faturamento}
      a cidade com menor faturamento é  = {cidade_menor_faturamento}
      
      ''')

print('''Hipotese:
      
      Comportamento de consumo  pode ser diferente entre cidades.
       
       Decisão: 
      
       Realizar levantamento de produtos que possuem  maior 
       participação em cada cidade antes de definir investimento.
       Cabe uma  pesquisa ... 
              
      ''')


# analise mensal 


df["Mês"] = df['Data'].dt.to_period('M')
# print(df['Mês'])

vendas_mensais = (
    df.groupby('Mês')['Faturamento'].sum().sort_index()
         
)

print(f'''
      
      Faturamento mensal 
      {vendas_mensais}
      
      ''')

# melhor mês de venda

melhor_mes = vendas_mensais.idxmax()
pior_mes  = vendas_mensais.idxmin()

print('Pior mes ', pior_mes)
print('Melhor mês', melhor_mes)

print('Existe um crescimento no decorrer do meses')

print('Investigar os meses de maior e menor faturamento')
print('identitificar  possiveis oportunidade, identificar padões')

# venda individual

melhor_venda_individual =  df.loc[df['Faturamento'].idxmax()]

print('Melhor venda individual ', melhor_venda_individual)



# DECISÃO FINAL 

print(f'''decisão final:  
      
      produto prioritario {produto_volume}
      
      Justificativa:
      
      O produto apresenta o maior faturamento entre todos.
      
      ESTRATÉGIA:
      
      1 - AUMENTO DO VALUME DE VENDA DESSE PRODUTO 
      2 - VENDA COMBINADAS COM O PRODUTO DE MAIOR FATURAMENTO
      3 - INVESTIGAR COMPORTAMENTOS DE VENDAS POR CIDADE 
      4 - MONITORAR FATURAMENTO MENSALMENTE
      
      5 - COMPARAR OS RESULTADOS APÓS A ESTRATÉGIA APLICADA      
          
      ''')

# CONCLUSÃO 


print('''CONCLUSÃO: 
      
      A    analise mostrar quantidade de vendas e faturamento 
      são indicadores diferentes 
      
      O produto mais vendido não é o que possui o maior faturamento
      e também não é o mais importante financeiramemnte falando.
      
      - > pegar os número e transforma em evidências. 
     o apoio a decisão estratégica da empresa.   
    
      
      ''')




