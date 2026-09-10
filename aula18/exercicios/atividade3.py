import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# EXERCÍCIO 3: Previsão de Crescimento de Plantas

# Dados de dias desde plantio vs altura da planta
dias = np.array([10, 20, 30, 40, 50]).reshape(-1, 1)
altura_cm = np.array([5, 12, 18, 25, 30])

# Criar o modelo
modelo = LinearRegression()

# Treinar o modelo
modelo.fit(dias, altura_cm)

# Prever a altura após 60 dias
previsao = modelo.predict([[60]])

print("Altura prevista após 60 dias:",
      round(previsao[0], 2), "cm")

# Gráfico
plt.scatter(dias, altura_cm, color="blue", label="Dados reais")

plt.plot(dias,
         modelo.predict(dias),
         color="red",
         label="Regressão linear")

plt.xlabel("Dias desde o plantio")
plt.ylabel("Altura (cm)")
plt.title("Crescimento da Planta")
plt.legend()
plt.grid()
plt.show()