# José Ignacio Menchaca Castro
# 215818166
from random import randint

filas = 3
columnas = 4
matriz = []

for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        matriz[i].append(randint(0, 100))
    print(matriz[i])
