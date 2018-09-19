val1 = 4
val2 = 6


def sum1():
    return print(val1 + val2)


def sum2(value_1, value_2):
    return print(value_1 + value_2)


def divisibles():
    for i in range(1, 26):
        if i % 7 == 0:
            print(i)


sum1()
sum2(val1, val2)
divisibles()
