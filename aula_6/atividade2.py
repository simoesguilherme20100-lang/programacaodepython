import statistics


# Dados dos alunos
def obter_alunos():
    alunos = [
        {"nome": "Ana", "nota": 8.5},
        {"nome": "Bruno", "nota": 7.0},
        {"nome": "Carlos", "nota": 9.0},
        {"nome": "Daniela", "nota": 8.5},
        {"nome": "Eduardo", "nota": 6.5},
        {"nome": "Fernanda", "nota": 7.5},
        {"nome": "Gabriel", "nota": 8.5},
        {"nome": "Helena", "nota": 9.5},
        {"nome": "Igor", "nota": 7.0},
        {"nome": "Juliana", "nota": 8.0}
    ]

    return alunos


# Extrai as notas de todos os alunos
def extrair_notas(alunos):
    return [aluno["nota"] for aluno in alunos]


# Calcula as estatísticas
def calcular_estatisticas(notas):
    return {
        "média": statistics.mean(notas),
        "mediana": statistics.median(notas),
        "moda": statistics.mode(notas),
        "amplitude": max(notas) - min(notas),
        "desvio padrão": statistics.stdev(notas),
        "menor nota": min(notas),
        "maior nota": max(notas)
    }


# Exibe todos os alunos
def exibir_alunos(alunos):
    print("\n===== ALUNOS =====")

    for aluno in alunos:
        print(f"{aluno['nome']}: {aluno['nota']:.2f}")


# Exibe as estatísticas
def exibir_estatisticas(estatisticas):
    print("\n===== ESTATÍSTICAS =====")

    print(f"Média:          {estatisticas['média']:.2f}")
    print(f"Mediana:        {estatisticas['mediana']:.2f}")
    print(f"Moda:           {estatisticas['moda']:.2f}")
    print(f"Amplitude:      {estatisticas['amplitude']:.2f}")
    print(f"Desvio padrão:  {estatisticas['desvio padrão']:.2f}")
    print(f"Menor nota:     {estatisticas['menor nota']:.2f}")
    print(f"Maior nota:     {estatisticas['maior nota']:.2f}")


# Programa principal
def main():
    alunos = obter_alunos()

    # Extrai as notas de todos os alunos
    notas = extrair_notas(alunos)

    # Calcula as estatísticas
    estatisticas = calcular_estatisticas(notas)

    # Mostra os resultados
    exibir_alunos(alunos)
    exibir_estatisticas(estatisticas)


if __name__ == "__main__":
    main()