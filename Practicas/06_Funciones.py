import webbrowser
import os



# El orden es importante --> Primero defino, luego uso.


def al_cuadrado(parametro):
    resultado = parametro * parametro
    return resultado


print(al_cuadrado(5))

miVariableGlobal = '''Variable 
    GLOBAL tiene visibilidad en  
    todo el módulo'''


def funcionPrintaTodasVariables():
    miVariableLocal = '''Variable 
    LOCAL solo tiene visibilidad 
    en el bloque de la función'''
    resultado = miVariableGlobal + "\n" + miVariableLocal
    return resultado


print(funcionPrintaTodasVariables())


# print(miVariableLocal)
# print(miVariableGlobal)


###################      PASO POR VALOR       #####################
def doblar_valorSimple(numero):
    numero *= 2


n = 10
doblar_valorSimple(n)
print(n)


###################      PASO POR REFERENCIA       #####################
def doblar_valoresComplejo(numeros):
    for i, n in enumerate(numeros):
        numeros[i] *= 2


ns = [10, 50, 100]
doblar_valoresComplejo(ns)
print(ns)

###################      FUNCIONES de Python       #####################
# Fichero
# a Añade, w reescribe --> de que manera abro el fichero.
f = open("hola.txt", "a")
f.write("Hola este es mi contenido")
f.close()

f = open("hola.txt", "w")
f.write("Empezamos de nuevo")
f.close()

# import os
f = open("hola.html", "a")
f.write("<html><body><h1>HELLO World!</h1></body></html>")
f.close()
os.system("start chrome hola.html")
# import webbrowser
webbrowser.get('chrome').open_new(
    "file:///hola.html")
