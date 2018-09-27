'''
José Ignacio Menchaca Castro
215818166
'''

from random import randint


def suma(val1, val2):
    return print(val1+val2)


def random(val1, val2):
    return print(randint(val1, val2))


def ecuacion(val1, val2):
    x = 0
    if val1 != 0:
        x = val2/val1
    else:
        if val2 != 0:
            print('Solucion imposible')
        else:
            print('Indeterminada')
    return print(x)


def menu():
    val1 = float(input('Ingrese valor 1: '))
    val2 = float(input('Ingrese valor 2:'))
    print("""
    1.- Suma
    2.- valor ramdom
    3.- ecuación de primer grado
    """)
    while True:
        opc = int(input())
        if opc == 1:
            suma(val1, val2)
            break
        elif opc == 2:
            random(val1, val2)
            break
        elif opc == 3:
            ecuacion(val1, val2)
            break
        else:
            print('Opción invalida!')
            print('Elija de nuevo: ')


menu()
