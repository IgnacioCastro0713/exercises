def cycle_for():
    while True:
        val = int(input('Ingrese valor: '))
        for i in range(0, 11):
            print(val, "x", int(i), "=", int(i*val))
        opc = input('¿Otra vez?: ')
        if opc == 'No' or opc == 'no':
            print('Gracias!')
            break


cycle_for()

# jose.adolfo.castillo@hotmail.es
