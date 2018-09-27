lista = []
num = int(input('Define el tamaño de la lista:'))

for i in range(0, num):
    val = int(input('valor '+str(i+1)+': '))
    lista.append(val)

par = 0
impar = 0

for x in range(0, len(lista)):
    if x % 2 == 0:
        par += 1
    else:
        impar += 1

print('Pares: ', par, 'impares: ', impar)
