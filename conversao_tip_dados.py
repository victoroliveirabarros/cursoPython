#convertendo tipos de dados
INTEIRO = 25
FLOAT = 4.78
COMPLEX = 2+1j
STRING = "TEXTO"

#convertendo inteiro para float
INT_FLOAT = float(INTEIRO)
print(type(INT_FLOAT))

#convertendo float para inteiro
FLOAT_INT = int(FLOAT)
print(type(FLOAT_INT))

#convertendo inteiro para complexo
INT_COMPLEX = complex(25)
print(type(INT_COMPLEX))

#convertendo float para texto (string)
FLOAT_STRING = str(FLOAT)
print(type(FLOAT_STRING))