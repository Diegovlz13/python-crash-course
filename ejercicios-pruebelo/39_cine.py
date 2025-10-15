edad = -1
while True:
    edad = int(input("¿Cual es tu edad?\n-> (presione 0 para salir): "))
    if edad == 0:
        break
    if edad < 3:
        print("Su entrada será gratis.")
    elif edad >= 3 and edad <= 12:
        print("Tienes que pagar 8 euros.")
    elif edad > 12:
        print("Tienes que pagar 12 euros.")