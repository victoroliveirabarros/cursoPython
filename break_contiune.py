#Break, continue e pass statements
lista_loop = ["Um", "Dois", "Três", "Quatro"]

#break
for i in lista_loop:
    if i == "Dois":
        break

print("Você achou o Dois")

#continue
for i in lista_loop:
    if i == "Três":
        continue
    print(i)

#pass
contador = 0
while contador <= 100:
    pass