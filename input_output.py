#Input e Output

#input
nome = str(input("Digite o seu nome: "))
idade = int(input("Digite a sua idade: "))

#output
print("Olá, {0}, sua idade é {1} ".format(nome, idade))
print("Olá, %s, sua idade é %i" % (nome, idade))