# Ejercicio 5
import random

__author__ = "Barbara Herrera Flores"

continuar = True
while continuar == True:
    # El usuario decide con que rango de valores jugar
    print("Introduce un rango de dos numeros para jugar, por ejemplo entre 5 y 18 ")
    num1 = input("Numero 1: ")
    num2 = input("Numero 2: ")

    # Comprobar intups para evitar salida abrupta en caso de error
    while num1.isdigit() == False or int(num1) < 1 or int(num2) == int(num1):
        num1 = input("Error, numero 1: ")
        num2 = input("Error, numero 2: ")

    if int(num1) > int(num2):
        aux = num1
        num1 = num2
        num2 = aux

    # Hay que castear los inputs, son strings en python.
    pensado = random.randrange(int(num1), int(num2))  # Generar valores aleatorios
    jugada = input("Introduce un numero para adivinar entre " + num1 + " y " + num2 + " :")

    if int(pensado) == int(jugada):
        print("Felicidades, adivinaste el numero ", pensado)
        continuar = False
    else:
        again = ""
        # Bucle para jugar otra vez en caso de no acertar
        while again not in ("S", "N"):
            # Upercase para aceptar minusculas.
            again = input("Lo siento, no lo has adivinados ¿quieres jugar otra vez? S/N ").upper()
            if "S" == again:
                continuar = True
            elif again == "N":
                continuar = False
