nom = input("Introduce un nombre se usuario: ")
key = input("Introduce una contraseña: ")
CONST_NAME = "Barbara"
CONST_KEY = "123"
contador = 0
while contador < 3:
    if nom == CONST_NAME:
        if key != CONST_KEY:
            key = input("Contraseña incorrecta, intnetalo otra vez: ")
            contador += 1
        else:
            print("Contraseña correcta")
            break
    else:
        nom = input("Usuario incorrecto, intentalo otra vez: ")
        key = input("Introduce una contraseña: ")
        contador += 1
    if not contador < 3:
        print("Has fallado demasiadas veces.")
