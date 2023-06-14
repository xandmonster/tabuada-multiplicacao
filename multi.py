import os #importando biblioteca para aceitar comandos do terminal do sistema operacional
import time #importando biblioteca para poder da um tempo antes de executar proxima acao
from random import randint #importando biblioteca para gerar numeros pseudo aleatorios


print("---\ntabuada de multiplicação\n---")

#funcao do jogo da tabuada
def tabuada():
    #usando try para impedir que o usuario insira valor invalido
    try: 
        numero_jogado = int(input("Qual é o valor a ser jogado? "))
    except ValueError:
        print("Digite um número válido")
        tabuada()
    #loop para o usuario continuar jogando
    while True: 
        fator_aleatorio = randint(1, 10) 
        #usando try para impedir que o usuario insira valor invalido
        try:
            pergunta = int(input("Quanto é {} x {} ? ".format(numero_jogado, fator_aleatorio))) 
        except ValueError:
            print("Digite um número válido")
            continue

        #caso o usuario acerte a questao exibe uma mensagem dizendo que ele acertou e limpa a tela
        if fator_aleatorio * numero_jogado == pergunta: 
            print("você acertou!")
            time.sleep(1)
            os.system('cls')
        #caso o usuario erre ele pode sair do jogo ou jogar novamente
        else: 
            opcao = input("você errou - digite 'a' para jogar de novo ou 's' para sair ") 
            if opcao == 's':
                break
            else:
                tabuada()

            
#chamando a funcao
tabuada()

