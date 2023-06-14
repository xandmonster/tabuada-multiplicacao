#importando bibliotecas
from time import sleep
from os import system
import random

print("---\nTabuada de Divisão\n---") #titulo na tela

#funcao do jogo da tabuada
def tabuada():
    try: #usando try para impedir que o usuario insira valor invalido
        numero_jogado = int(input("Qual numero a ser jogado? "))
        while True: #loop para o usuario continuar jogando
            fator_aleatorio = random.randrange(numero_jogado, (numero_jogado*10) + numero_jogado, numero_jogado)
            try: #usando try para impedir que o usuario insira valor invalido
                pergunta = int(input("Quando é {} : {}? ".format(fator_aleatorio, numero_jogado)))
                if fator_aleatorio / numero_jogado == pergunta:
                    print("Você acertou")
                    sleep(1)
                    system('cls')
                else:
                    #quando o usuario erra ele tem a opcao de sair ou jogar de novo
                    opcao = input("Você errou! Digite 'a' para jogar de novo ou 's' para sair ")
                    if opcao == 'a':
                        tabuada()
                    else:
                        break
            except ValueError:
                print("Digite um valor correto")
                continue
    except ValueError:
        print("Digite um valor correto")
        tabuada()



tabuada()