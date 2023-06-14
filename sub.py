#importando bibliotecas
import os
import time
from random import randint

print("---\nTabuada de Subtração\n---") #titulo na tela

#funcao do jogo da tabuada
def tabuada():
    try: #usando try para impedir que o usuario insira valor invalido
        numero_jogado = int(input("Qual numero vai ser jogado? "))
    except ValueError:
        print("Digite um número válido")
        tabuada()
    while True: #loop para o usuario continuar jogando
        fator_aleatorio = randint(1, 20)
        try: #usando try para impedir que o usuario insira valor invalido
            pergunta = int(input("Quanto é {} - {}? ".format(fator_aleatorio, numero_jogado)))
            if fator_aleatorio - numero_jogado == pergunta:
                print("Você acertou")
                time.sleep(1)
                os.system('cls')
            else:
                #quando o usuario erra ele tem a opcao de sair ou jogar de novo
                opcao = input("Você errou! Digite 'a' para jogar novamente ou 's' para sair: ")
                if opcao == "a":
                    tabuada()
                else:
                    break
                print("Você errou!")
        except ValueError:
            print("Digite um numero valido")
            continue
    

tabuada()