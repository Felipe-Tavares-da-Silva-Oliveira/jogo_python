import random

print("####################################")
print("Bem vindo ao jogo da adinhação")
print("####################################")

numero_secreto = random.randrange(0, 101)
total_de_tentativas = 0
rodada = 1
print("Qual o nível de dificuldade?")
print("(1) fácil (2) Médio (3) Difícil")

nivel = int(input("Defíne o Nível:  "))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
elif(nivel == 3):
    total_de_tentativas = 5

for rodada in  range(1, total_de_tentativas):

    print("tentativa {} de {}".format(rodada,total_de_tentativas))

    chute_str = input("Digite o seu numero:  ")

    chute = int(chute_str)
    if(int(chute_str) < 1) or (chute > 100):
        print('numero invalido  - o número deve estar entre 1 e 100')
        continue
    print("você digitou ", chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto


    if (acertou):
        print("parabens você acertou")
        break
    else:
        if(maior):
            print("O seu chute foi maior do que o número secreto!")
        if(menor):
            print("O seu chute foi menor do que o número secreto!")
    rodada = rodada + 1
    print("FIM DE JOGO")