import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# EXERCÍCIO 2: Previsão de Consumo de Energia

# Dados de temperatura x consumo de energia
temperaturas = np.array([15, 20, 25, 30, 35]).reshape(-1, 1)
consumo_kwh = np.array([120, 100, 90, 110, 150])

# Criar o modelo
modelo = LinearRegression()

# Treinar o modelo
modelo.fit(temperaturas, consumo_kwh)

# Prever o consumo para uma temperatura de 40°C
previsao = modelo.predict([[40]])

print("Consumo previsto para 40°C:",
      round(previsao[0], 2), "kWh")

# Exibir coeficientes
print("Coeficiente angular:", modelo.coef_[0])
print("Intercepto:", modelo.intercept_)

# Gráfico
plt.scatter(temperaturas, consumo_kwh,
            color="blue", label="Dados reais")

plt.plot(temperaturas,
         modelo.predict(temperaturas),
         color="red", label="Regressão linear")

plt.xlabel("Temperatura (°C)")
plt.ylabel("Consumo (kWh)")
plt.title("Temperatura vs Consumo de Energia")
plt.legend()
plt.grid()
plt.show()
