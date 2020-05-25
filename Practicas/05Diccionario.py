################################################################
###################      DICCIONARIOS       ####################
################################################################

# Mi primer diccionario
diccionario = {'uno': 1, 'dos': 2, 'tres': 3}
print(type(diccionario))

# Accediendo a los valores
diccionario = {'uno': 1, 'dos': 2, 'tres': 3}
print(diccionario['uno'])


# Eliminando
diccionario = {'uno': 1, 'dos': 2, 'tres': 3}
del(diccionario['dos'])
print(diccionario)

# Pertenencia
dic = {'uno': 1, 'dos': 2}
print("uno" in dic)
print("tres" in dic)

# Modificiaciones
dic_coche = {
    'marca': "seat",
    'modelo': 'Ibiza'
}
print(dic_coche["modelo"])
dic_coche["modelo"] = "Cordoba"
print(dic_coche["modelo"])
print(dic_coche)

# Eliminando!
dic = {'uno': 1, 'dos': 2}
print(dic)
dic.clear()
print(dic)

# El metodo Get es muy útil
dic = {'uno': 1, 'dos': 2}
dic["uno"]
dic["tres"]
dic.get("uno")
dic.get("tres")

# El metodo pop retorna y elimina
dic = {
    'uno': "primer elemento",
    'dos': "segundo element",
    'tres': "tercer elemento"}
print(dic.pop('uno'))
print(dic)

# REFERENCIA
coche1 = {
    'marca': "seat",
    'modelo': 'Ibiza'
}
coche2 = coche1
print(coche1)
print(coche2)
coche1["modelo"] = "Cordova"
print(coche1)
print(coche2)

# VALOR
coche1 = {
    'marca': "seat",
    'modelo': 'Ibiza'
}
coche2 = coche1.copy()
print(coche1)
print(coche2)
coche1["modelo"] = "Cordova"
print(coche1)
print(coche2)

# RECORRIENDO
capitals = {
    'Lleida': "Terra ferma",
    'Tarragona': "Imperial",
    'Girona': "Tramuntana",
    'Barcelona': "Possat guapa que et fa falta"
}

for key in capitals.keys():
    print(key)
for value in capitals.values():
    print(value)
for ciutat, slogan in capitals.items():
    print(ciutat+" --- "+slogan)