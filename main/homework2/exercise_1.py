from math import sqrt

a = float(input("valor de a: "))
b = float(input("valor de b: "))
c = float(input("valor de c: "))

if a == 0:
    print('La ecuacion no tiene solucion. ')
else:
    z1 = sqrt(b ** 2 - 4 * a * c)
    z2 = sqrt(b * b - 4 * a * c)
    x1 = (-b + z1) / (2 * a)
    x2 = (-b - z2) / (2 * a)
    print(x1, x2)
