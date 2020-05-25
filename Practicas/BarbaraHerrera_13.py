coches = {
    '1234': ["Ferrari", "Mustang"]
}

menu = """
+---------------------------+
|   (1) Añadir coche        |
|   (2) Mostrar coche       |
|   (3) Listar coches       |
|   (4) Terminar            |
+---------------------------+
"""


# Funciones
def checkmatricula(key):
    if key in coches:
        return True


def addcoche(cars):
    matricula = input("Introduce la matricula: ").__str__().upper()
    cont = 0
    while checkmatricula(matricula):
        matricula = input(
            "La matricula se encuentra en el sistema, introduzca una matricula valida: ").__str__().upper()
        cont += 1
        if cont >= 3:
            print("Demasiados intentos")
            return
    marca = input("Introduce la marca: ").__str__()
    modelo = input("introduce el modelo: ").__str__()
    cars.update({matricula: [marca, modelo]})


def mostrarcoche():
    mat = input("Introduce la matricula: ").__str__().upper()
    if checkmatricula(mat):
        coche = coches.get(mat)
        print("--------------------------------")
        print("Datos del coche:")
        print("Matricula: " + mat)
        print("Marca: " + coche[0])
        print("Modelo: " + coche[1])
        print("--------------------------------")
    else:
        print("Este coche no existe")
        return


def listar():
    print("--------------------------------")
    print("Lista de coches: ")
    for key, value in coches.items():
        print(key, value[0])
    print("--------------------------------")


aux = True
while aux:
    print(menu)
    p = input("Elige una opcion: ")
    while not p.isdigit() or int(p) > 4:
        print(menu)
        p = input("Error, introduce un numero del menu: ")
    int(p)
    if int(p) == 1:
        addcoche(coches)
    if int(p) == 2:
        mostrarcoche()
    if int(p) == 3:
        listar()
    if int(p) == 4:
        exit()
