import random

def jogo_adivinhacao():
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Estou pensando em um número entre 1 e 100...")
    
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    while not acertou:
        chute = input("Digite seu palpite: ")
        if not chute.isdigit():
            print("Por favor, digite apenas números.")
            continue
        
        chute = int(chute)
        tentativas += 1
        
        if chute < numero_secreto:
            print("Muito baixo! Tente um número maior.")
        elif chute > numero_secreto:
            print("Muito alto! Tente um número menor.")
        else:
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            acertou = True

# Executa o jogo
jogo_adivinhacao()
