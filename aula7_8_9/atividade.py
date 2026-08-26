import numpy as np

# Criando uma matriz 5x5 com valores aleatórios entre 0 e 100
matriz = np.random.randint(0, 101, size=(5, 5))

# Calculando a média de cada linha
medias = np.mean(matriz, axis=1)

# Encontrando o maior e o menor valor da matriz
maior = np.max(matriz)
menor = np.min(matriz)

print("Matriz:")
print(matriz)

print("\nMédia de cada linha:")
print(medias)

print("\nValor máximo:", maior)
print("Valor mínimo:", menor)