values = [int(input("Valor 1: ")), int(input("Valor 2: ")), int(input("Valor 3: "))]

for i in range(1, len(values)):
    for j in range(len(values) - i):
        if values[j + 1] < values[j]:
            res = values[j]
            values[j] = values[j + 1]
            values[j + 1] = res

print("\nValores ordenados:", str(values).strip('[]'))
