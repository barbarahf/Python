__author__ = "Barbara Herrera Flores"
dni = input("Introduce tu DNI sin letra: ")
#Comprobar inputs
while dni.isdigit() == False or len(dni) != 8:
    dni = input("Error, introduce un DNI valido: ")
letras = "TRWAGMYFPDXBNJZSQVHLCKE"
valor = int(dni) % 23
print("Tu dni con letra es: " + dni + letras[valor])
