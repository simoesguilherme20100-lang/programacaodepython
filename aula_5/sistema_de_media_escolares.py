# Variável global
escola = input("Digite o nome da Escola: ")

def calcular_media(nota1, nota2, nota3):
    # nota1, nota2 e nota3 são parâmetros
    media = (nota1 + nota2 + nota3) / 3
    # media é uma variável local
    return media

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

# Programa principal
nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media_final = calcular_media(nota1, nota2, nota3)
situacao = verificar_situacao(media_final)

print("\n--- RESULTADO ---")
print("Escola:", escola)
print("Aluno:", nome)
print("Média:", round(media_final, 2))
print("Situação:", situacao)