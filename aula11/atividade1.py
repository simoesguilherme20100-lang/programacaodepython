import pandas as pd
import matplotlib.pyplot as plt

# Ler os dados
df = pd.read_csv("dados_estudantes.csv")

# 1. Gráfico de notas por gênero
media_genero = df.groupby("gender")["exam_score"].mean()

plt.figure()
media_genero.plot(kind="bar")
plt.title("Média de notas por gênero")
plt.xlabel("Gênero")
plt.ylabel("Média das notas")
plt.show()


# 2. Gráfico de horas de estudos x notas
plt.figure()
plt.scatter(df["study_hours_per_day"], df["exam_score"])
plt.title("Horas de estudos x notas")
plt.xlabel("Horas de estudo por dia")
plt.ylabel("Nota")
plt.show()


# 3. Média de notas por idade
media_idade = df.groupby("age")["exam_score"].mean()

plt.figure()
media_idade.plot(kind="bar")
plt.title("Média de notas por idade")
plt.xlabel("Idade")
plt.ylabel("Média das notas")
plt.show()


# 4. Análise: média de horas de estudos
media_horas = df["study_hours_per_day"].mean()

print("Média de horas de estudos por dia:", round(media_horas, 2))


# 5. Gráfico de média de notas por idade
plt.figure()
media_idade.plot(kind="line", marker="o")
plt.title("Média de notas por idade")
plt.xlabel("Idade")
plt.ylabel("Média das notas")
plt.grid()
plt.show()