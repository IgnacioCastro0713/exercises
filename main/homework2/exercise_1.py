from math import sqrt

a = float(input("valor de a: "))
b = float(input("valor de b: "))
c = float(input("valor de c: "))

if a == 0 and a < 0:
    print("error, 'a' no debe ser cero o menor a cero")
else:
    x1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - sqrt(b * b - 4 * a * c)) / (2 * a)
    print(x1, x2)
