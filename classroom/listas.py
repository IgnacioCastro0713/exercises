lista = []
suma = 0
suma2 =0
media = 0.0
varianza =0.0

while True:
    opc = input('desea ingresar datos? S/N: ')
    if opc.lower() == 's':
        dato = int(input('ingrese valor:'))
        lista.append(dato)
    else:
        break

for i in range(0, len(lista)):
    suma = suma+lista[i]
    suma2 = suma2 + (lista[i]-suma/len(lista)**2)

media = suma/len(lista)
varianza = suma2/len(lista)

print(lista)
print('La varianza es: ', varianza)
print('La suma es:', suma)
print('La media es:', media)
