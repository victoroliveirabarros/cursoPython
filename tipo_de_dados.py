#tipo de dado booleano
Verdadeiro = True #1
Falso = False #0

#tipo de dado numérico
#inteiro
inteiro = 10
print(type(inteiro))

#float
float_num = 12.67
print(type(float_num))

#complexos
complex_num = 1+0j
print(type(complex_num))

print("------------------")

#tipo de dados de texto
str_1 = "Esta é uma String"
str_2 = "Esta é outra String"

#indexando
print(str_1[0])

#slice
print(str_1[0:4])

#concatenando strings
print(str_1 + " " + str_2)

#tamanho de uma string
print(len(str_1))

#repetindo uma string
print(str_2*5)

#função upper
print(str_1.upper())

#função lower
print(str_1.lower())

print("----------------")

#tipo de dado LISTA
lista = [6, 3, 8, 90, 4, 2]

#funcao append()
lista.append(89)
print(lista)

#deletando itens da lista
del lista[-1]
print(lista)

#ordenando itens da lista (crescente)
lista.sort()
print(lista)

#ordenando itens da lista (decrescente)
lista.reverse()
print(lista)

#listas podem conter todos os tipos de dados do python
lista_exemplo = [13, 2+0j, 5.67, "str", [1, 2, 3], False]

print("------------------")

#tipo de dado TUPLA
tupla = (1, 2, 3, 4)

#indexing
tupla[0]

#slicing
tupla[0:-1]


print("-------------------")

#tipo de dados dicionário
dicionario = {"Chave1":"Valor1", "Chave2":"Valor2"}

#indexing
dicionario['Chave1']
print(dicionario['Chave1'])

#adicionar entradas
dicionario["Chave3"] = "Três"
print(dicionario)

#modificando dados
dicionario["Chave3"] = 3
print(dicionario)

#removendo dados
dicionario.pop("Chave2")
print(dicionario)