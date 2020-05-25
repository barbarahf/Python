# Defino un diccinario con cosas y estructuras X
dic_Objetos = {
    '4564748F': ["Maria", "Fernandez", 1/1/2000, 8],
    '3452GHF': "Coche Robado",
    '4578JPR': ["Yamaha", "XMax", 250, "blanca"],
    'Brasil': "Rio de Janeiro"
}

# printo los elementos de la lista
# Sé que es un DNI, con lo que sé que tipo de objeto hay y que datos tiene.
print(dic_Objetos.get("4564748F"))
# Esto es una matricula
print(dic_Objetos.get("4578JPR"))


def eliminaCocheRobado(dic_Objetos):
    dic_Objetos.pop("3452GHF")


# eliminamos el elementos con clave = 3452GHF --> El coche robado
eliminaCocheRobado(dic_Objetos)

print(dic_Objetos)
print(dic_Objetos.get("3452GHF"))  # --> None, ya no está.


def muestraCoche(dic_Objetos, matricula):
    coche = dic_Objetos.get(matricula)
    print("***************************")
    print("El coche tiene marca: " +
          coche[0] + " y modelo: " + coche[1] + " color " + coche[3])


def clavesDic(dic_Objetos):
    for key in dic_Objetos.keys():
        print(key)


muestraCoche(dic_Objetos, "4578JPR")
clavesDic(dic_Objetos)
