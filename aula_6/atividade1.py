import statistics

# Salários das empresas
empresas = {
    "Empresa 1": [2500, 2800, 3000, 9500, 12000],
    "Empresa 2": [5000, 5200, 5300, 5400, 5500],
    "Empresa 3": [1000, 2000, 8000, 15000, 20000],
    "Empresa 4": [3500, 4000, 4200, 4300, 6000],
    "Empresa 5": [1200, 1500, 1800, 2500, 10000]
}

# Análise estatística
for empresa, salarios in empresas.items():
    media = statistics.mean(salarios)
    mediana = statistics.median(salarios)
    amplitude = max(salarios) - min(salarios)
    variancia = statistics.pvariance(salarios)
    desvio_padrao = statistics.pstdev(salarios)

    # Moda
    modas = statistics.multimode(salarios)
    if len(modas) == len(salarios):
        moda = "Não há"
    else:
        moda = modas

    print(f"\n{empresa}")
    print(f"Média: R$ {media:,.2f}")
    print(f"Mediana: R$ {mediana:,.2f}")
    print(f"Moda: {moda}")
    print(f"Amplitude: R$ {amplitude:,.2f}")
    print(f"Variância: {variancia:,.2f}")
    print(f"Desvio padrão: R$ {desvio_padrao:,.2f}")

# Justificativa da escolha
print("\n--- ESCOLHA ---")
print("Eu escolheria a Empresa 2.")
print("Ela possui salários entre R$ 5.000 e R$ 5.500,")
print("apresentando baixa amplitude e baixo desvio padrão.")
print("Isso significa que os salários são mais estáveis e previsíveis.")
print("Apesar de a Empresa 3 ter a maior média,")
print("ela apresenta grande variação entre os salários.")