import random

def adivinhador():
    numero_secreto = random.randint(1, 100)
    for tentativa in range(5):
        numero_adivinhado = int(input("Digite um número: "))
        if numero_adivinhado == numero_secreto:
            print("Parabéns, você acertou!")
            return
        else:
            if numero_adivinhado < numero_secreto:
                print("O número é maior que", numero_adivinhado)
            else:
                print("O número é menor que", numero_adivinhado)
    print("Você perdeu! O número secreto era", numero_secreto)

if name == "main":
    adivinhador()
