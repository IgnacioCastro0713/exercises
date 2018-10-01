# José Ignacio Menchaca Castro
# 215818166
lista = ['Ana', 'Luis', 'Pedro', 'Juan']
x = 0

while True:
    print('Seleciona una opción de la lista a remplazar: ')
    for i in lista:
        x += 1
        print(x, '.-', i)

    remove = int(input('Opcion: '))
    lista.remove(lista[remove - 1])
    print('Lista: ', lista)
    replace = input('Escribe el nuevo nombre de la lista: ')
    lista.insert(remove - 1, replace.capitalize())
    print('Lista: ', lista)

    ask = input('¿Desea terminar el programa? s/n: ')
    if ask.lower() != 'n':
        break
