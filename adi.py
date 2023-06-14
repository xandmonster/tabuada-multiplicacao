#importando bibliotecas
import os
import time
from random import randint

#titulo na tela
print("---\ntabuada de adição\n---")


#funcao do jogo da tabuada
def tabuada():
    try: #usando try para impedir que o usuario insira valor invalido
        numero_jogado = int(input("Digite o numero a ser jogado: "))
    except ValueError: 
        print("Digite um valor válido")
        tabuada()

    while True: #loop
        fator_aleatorio = randint(1, 20) #usando numero aleatorio entre 1 e 20
        try: #try para caso o usuario digitar errado
            pergunta = int(input("Quanto é {} + {}? ".format(numero_jogado, fator_aleatorio)))
        except ValueError:
            print("Digite um valor válido")
            continue
        if pergunta == fator_aleatorio + numero_jogado:
            print("Você acertou!")
            time.sleep(1)
            os.system("cls")
        else:
            #quando o usuario erra ele tem a opcao de sair ou jogar de novo
            opcao = input("Você errou! Digite 'a' para jogar de novo ou 's' para sair: ")
            if opcao == "a":
                tabuada()
            elif opcao == "s":
                break

tabuada()