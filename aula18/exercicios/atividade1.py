import numpy as np
from sklearn.linear_model import LinearRegression

# Dados históricos
horas_estudo = np.array([2, 4, 6, 8, 10]).reshape(-1, 1)
notas = np.array([5.0, 6.5, 7.8, 8.5, 9.2])

# Criar o modelo
modelo = LinearRegression()

# Treinar o modelo
modelo.fit(horas_estudo, notas)

# Prever a nota para 7 horas de estudo
horas = np.array([[7]])
nota_prevista = modelo.predict(horas)

print("Nota prevista:", nota_prevista[0])

# Mostrar os coeficientes
print("Coeficiente:", modelo.coef_[0])
print("Intercepto:", modelo.intercept_)