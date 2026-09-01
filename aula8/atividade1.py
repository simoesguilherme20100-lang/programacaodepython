import matplotlib.pyplot as plt

ano = [2021, 2022, 2023, 2024, 2025, 2026]
vendas = [10000, 2000, 30000, 10000, 5000, 20000]

plt.plot(ano, vendas, marker='o')

plt.title('Vendas por Ano')
plt.xlabel('Ano')
plt.ylabel('Vendas')
plt.grid(True)

plt.show()