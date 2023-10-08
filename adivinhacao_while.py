print("####################################")
print("Bem vindo ao jogo da adinhação")
print("####################################")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1
while(rodada <= total_de_tentativas):

    print("tentativa {} de {}".format(rodada,total_de_tentativas))

    chute_str = input("Digite o seu numero:  ")

    chute = int(chute_str)
    print("você digitou ", chute)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto


    if (acertou):
        print("parabens você acertou")
    else:
        if(maior):
            print("O seu chute foi maior do que o número secreto!")
        if(menor):
            print("O seu chute foi menor do que o número secreto!")
    rodada = rodada + 1
    print("FIM DE JOGO")