#Desenvolvimento jogo guess the number

import random

contador = 0
guessNum = random.randint(1, 10)
placar_total = 0

nome = str(input("Digite o seu nome: "))
print("Olá, {0}! Seja bem vindo ao jogo Guess the Number!".format(nome))
print("Eu selecionei um número aleatório em uma sequência de 1 até 10. Você terá 3 chances para adiviná-lo")
print("Comece!")

while True:

    while contador < 3:

        numero = int(input("Digite um numero: "))
        contador += 1

        if numero < guessNum:
            print("O numero que você precisa adivinhar é maior!")

        elif numero > guessNum:
            print("O número que você adivinhar é menor!")

        elif numero == guessNum:
            print("Parabéns! Você descobriu o número {0}, em {1} tentativas!".format(guessNum, contador))  
            placar_total +=1
            break

    if (contador == 3) and (numero != guessNum):
        print("Você atingiu o número máximo de tentativas!")
        print("Jogo Finalizado!")

    else:
        print("Jogo Finalizado!")

    CONTINUE = str(input("Deseja recomeçar o game? (s/n)"))
    if CONTINUE == 's':
        contador = 0
        guessNum = random.randint(1, 10)
    else:
        break        

print("Nome: ", nome)
print("Sua pontuação total foi de: ", placar_total)   
print("Game finalizado!")
