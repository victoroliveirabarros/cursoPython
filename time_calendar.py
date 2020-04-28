#Módulo time & calendar para softwares em python
import time

#função time.time()
print(time.time())

#formatando e exibindo tempo local (atual)
tempo_local = time.asctime(time.localtime(time.time()))
print(tempo_local)

#retornando o calendario de determinado período
import calendar
calendario = calendar.month(2019, 1)
print(calendario)

#mensurando o tempo de execução de uma tarefa
print("Programa")
print(time.perf_counter())

#suspendendo temporariamente uma tarefa
time.sleep(5)
print("Hello World!!")
print(time.perf_counter())

