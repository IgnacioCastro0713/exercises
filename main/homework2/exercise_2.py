from random import randrange

price = int(randrange(1000))
while True:
    payment = int(input(f"Precio total: ${price}\nPago con:"))
    if payment < price:
        print("Dinero insuficiente!")
    else:
        print("cambio: ", payment-price, "\nGracias por su compra!")
        break
