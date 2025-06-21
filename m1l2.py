import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

repetir = "s"

while repetir == "s":
    longitud = int(input("Cuántos caracteres"))

    if longitud > 30:
        print(" El máximo permitido es 30 Intenta otra vez")
    else:
        contraseña = ""
        for i in range(longitud):
            contraseña = contraseña + random.choice(caracteres)

        print("Tu contraseña generada es:", contraseña)

    repetir = input("¿Quieres generar otra contraseña? (s/n): ")
