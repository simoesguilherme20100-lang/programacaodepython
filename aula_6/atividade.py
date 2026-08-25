import statistics


# 1ª frequência
frequencia1 = [1, 2, 3, 6, 4]

# 2ª frequência
frequencia2 = [1.5, 6.8, 9.7, 10.6]

# 3ª frequência
frequencia3 = [200, 300, 500, 700, 900, 400, 600]


def mean():
    media = statistics.mean(frequencia1)
    return media

def mode():
    moda =  statistics.mode(frequencia2)
    return moda

def median():
    mediana = statistics.median(frequencia3)
    return mediana


# Moda
print(mode())


# Mediana
print(median())


# Média
print(mean())