import matplotlib.pyplot as plt

medias_jose = [10, 5, 8, 9, 10, 5, 4]
meses = ['fev', 'mar', 'abril', 'maio', 'junho', 'julho', 'agosto']

plt.bar(meses, medias_jose)

plt.title('Média de José por Mês')
plt.xlabel('Mês')
plt.ylabel('Média')

plt.show()