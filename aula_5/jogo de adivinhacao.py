import random

# Variável global
tentativas_maximas = 5

def gerar_numero():
    numero = random.randint(1, 100)
    return numero

def verificar_palpite(palpite, numero):
    if palpite == numero:
        return "acertou"
    elif palpite < numero:
        return "maior"
    else:
        return "menor"

def jogar():
    numero = gerar_numero()

    print("=== JOGO DA ADIVINHAÇÃO ===")
    print("Tente adivinhar um número entre 1 e 100!")
    print("Você tem", tentativas_maximas, "tentativas.")

    for tentativa in range(1, tentativas_maximas + 1):
        palpite = int(input(f"\nTentativa {tentativa}: Digite seu palpite: "))

        resultado = verificar_palpite(palpite, numero)

        if resultado == "acertou":
            print(" Parabéns! Você acertou!")
            return
        elif resultado == "maior":
            print("O número secreto é MAIOR.")
        else:
            print("O número secreto é MENOR.")

    print("\nVocê perdeu!")
    print("O número secreto era:", numero)

jogar()