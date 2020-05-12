# cadena = "informática"
# print("a" in cadena)
# print("q" in cadena)
# # Slice
# cadena = "En un lugar de la Mancha"
# print(cadena[6:11])
# print(cadena[:18])
# #
# cad = "¡Oh capitán, mi capitán!"
#
# print(cad.capitalize())
# print(cad.swapcase())
# print(cad.title())
#
# print(cad.count("capitán"))
# print(cad.find("mi"))
#
# cad = "Ser o no ser"
# print(cad.startswith("S"))
# print(cad.startswith("m"))
# print(cad.startswith("n", 6))
#
# buscar = "nombre apellido"
# reemplazar_por = "Juan Pérez"
# print("Estimado Sr. nombre apellido:".replace(buscar, reemplazar_por))
#
# # Union y division
#
# texto = '''Con diez cañones por banda,
# Viento en popa, a toda vela,
# No corta el mar, sino vuela.
# Un velero bergantín'''
# versos = texto.splitlines()
# print(versos)
cad = input("Introduce una cadena: ")
print(cad[::-1])
