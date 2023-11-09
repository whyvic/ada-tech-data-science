numero_sorteado = 15
tentativas = 0

while tentativas <4:
    numero_escolhido = int(input("informe um numero entre 1 e 20: "))
    if numero_sorteado == numero_escolhido:
        print("voce ganhou")
        print("parabens, voce acertou")
        break
    else:
        print("voce perdeu, tente novamente")
    tentativas += 1