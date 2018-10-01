# José Ignacio Menchaca Castro
# 215818166
lista = ['Ana', 'Luis', 'Pedro', 'Juan']
x = 0
while True:
    if len(lista) >= 1:
        print('Seleciona la opción que deseas eliminar: ')
        for i in lista:
            x += 1
            print(x, '.-', i)

        remove = int(input('Opcion: '))
        lista.remove(lista[remove - 1])
        print('Lista: ', lista)

        ask = input('¿Desea terminar el programa? s/n: ')
        if ask.lower() != 'n':
            break
    else:
        print('Lista vacia: ', lista)
        break
