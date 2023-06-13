import os
import time
from random import randint


print("---\ntabuada de multiplicação\n---")


def tabuada():
    numero = int(input("Qual é o valor a ser jogado? "))
    while True:
        aleatorio = randint(1, 10)
        pergunta = int(input("Quanto é {} x {} ? ".format(numero, aleatorio)))
        if aleatorio * numero == pergunta:
            print("você acertou!")
            time.sleep(1)
            os.system("cls")
        else:
            option = input("você errou - digite 'a' para jogar de novo ou 's' para sair ")
            if option == 's':
                break
            else:
                tabuada()

            

tabuada()