#escolhendo qual o maior numero

numero1 = int(input("Digite o 1º número: "))
numero2 = int(input("Digite o 2º número: "))



#ordenando-os em ordem crescente
if (numero1 < numero2):
    print("Ordem crescente: {0}, {1}!".format(numero1, numero2))

elif(numero1 > numero2):
    print("Ordem Crescente: {0}, {1}".format(numero2, numero1))

else:
    print("São iguais")
