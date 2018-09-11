# José Ignacio Menchaca Castro
# 215818166

from time import sleep

X = 40
while True:
    ask = str(input('Escriba EXIT para salir: '))
    if ask.lower() != 'exit':
        y = int(input('Ingrese temperatura del cultivo:'))
        if y < X:
            print('Todo bien!')
        else:
            print('Tu cultvo esta en peligro!')
        sleep(3)
    else:
        break
