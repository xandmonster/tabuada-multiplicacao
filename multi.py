# aqui importo as bibliotecas
import os
import time
from random import randint

#menuzinho para mostrar do que se trata
print("---\ntabuada de multiplicação\n---")

#criando a função para o usuario jogar a tabuada 
def tabuada():
    numero = int(input("Qual é o valor a ser jogado? "))
    while True: #loop para o usuario continuar jogando
        aleatorio = randint(1, 10) #gera numero aleatoria entre 1 e 10
        pergunta = int(input("Quanto é {} x {} ? ".format(numero, aleatorio))) #pergunta para o usuario a tabuada
        if aleatorio * numero == pergunta: #condicao caso o usuario acertar
            print("você acertou!")
            time.sleep(1)
            os.system("cls")
        else: #condicao caso o usuario errar
            option = input("você errou - digite 'a' para jogar de novo ou 's' para sair ") 
            if option == 's':
                break
            else:
                tabuada()

            
#chamando a função criada
tabuada()