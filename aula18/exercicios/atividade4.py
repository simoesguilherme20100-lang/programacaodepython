import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# EXERCÍCIO 4: Dados de quantidade de fertilizante vs produção

fertilizante_kg = np.array([50, 100, 150, 200, 250]).reshape(-1, 1)
producao_ton = np.array([2.0, 3.5, 4.8, 5.5, 6.0])

# Criar o modelo de regressão linear
modelo = LinearRegression()

# Treinar o modelo
modelo.fit(fertilizante_kg, producao_ton)

# Prever produção com 300 kg de fertilizante
previsao = modelo.predict([[300]])

print("Produção prevista com 300 kg de fertilizante:",
      round(previsao[0], 2), "toneladas")

# Exibir os coeficientes
print("Coeficiente angular:", modelo.coef_[0])
print("Intercepto:", modelo.intercept_)

# Gráfico
plt.scatter(fertilizante_kg, producao_ton,
            color="blue", label="Dados reais")

plt.plot(fertilizante_kg,
         modelo.predict(fertilizante_kg),
         color="red",
         label="Regressão linear")

plt.xlabel("Fertilizante (kg)")
plt.ylabel("Produção (toneladas)")
plt.title("Quantidade de Fertilizante vs Produção")
plt.legend()
plt.grid()
plt.show()