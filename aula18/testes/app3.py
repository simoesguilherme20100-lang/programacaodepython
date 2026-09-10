

from sklearn.linear_model import LinearRegression
import numpy as np


venda = {

    'jan': 20000.0,
    'fer': 30000.0,
    'mar': 50000.0,

}

meses = np.array([1,2,3]).reshape(-1,1)
valores = np.array([20000.0,30000.0,50000.0])

modelo = LinearRegression()
modelo.fit(meses, valores)

proximo_mes = 4 
venda_prevista = modelo.predict([[proximo_mes]])[0]
print(f'previsao de vendas : {venda_prevista}')