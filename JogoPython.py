print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 43   ## <-- Digita o número "Secreto" que você desejar ##
total_tentativas = 3  ## escolhe a quantidade de tentativas ##

for rodada in range(1, total_tentativas + 1):                              ## Contador de tentativas ##
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Voce digitou", chute_str)
    chute = int(chute_str)

    if chute < 1 or chute > 100:                                          ## Verificar números entre 1 e 100##
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto


    if acertou:                   ## Mensagem de acerto ##
        print("Você acertou!")
        break
    else:                         ## Mensagem de erro + dica caso a tentativa seja menor ou maior que o número secreto##
        if maior:
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif menor:
            print("Você errou! O seu chute foi menor do que o número secreto.")


print("Fim do jogo")