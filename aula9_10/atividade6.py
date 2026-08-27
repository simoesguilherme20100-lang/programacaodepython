import numpy as np

# Array de 1 a 10
array = np.arange(1, 11)

# Adicionar 10 a todos os elementos
array_mais_10 = array + 10

# Transformar o array 1D em um array 2D (2x5)
array_2d = array_mais_10.reshape(2, 5)

print("Array após adicionar 10:")
print(array_mais_10)

print("\nArray 2D (2x5):")
print(array_2d)