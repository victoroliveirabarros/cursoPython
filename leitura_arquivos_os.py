#módulo os para leitura e escrita de arquivos

import os

#leitura de arquivos
file = os.open("C:/Users/victo/Documents/Curso Python/arquivo_leitura.txt", os.O_RDWR)
file_readed = os.read(file, 22)
#print(file_readed)

#escrita em arquivos
file_wrote = os.write(file, "\n Esta é uma String!".encode())
os.close(file)