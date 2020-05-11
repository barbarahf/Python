lista = ["El", "código", "fuente", "de", "los", "lenguajes", "imperativos", "encadena", "instrucciones", "una",
         "detrás", "de", "otra", "que", "determinan", "lo", "que", "debe", "hacer", "el", "ordenador", "en", "cada",
         "momento", "para", "alcanzar", "un", "resultado", "deseado", "Los", "valores", "utilizados", "en", "las",
         "variables", "se", "modifican", "durante", "la", "ejecución", "del", "programa.", "Para", "gestionar", "las",
         "instrucciones,", "se", "integran", "estructuras", "de", "control", "como", "bucles", "o", "estructuras",
         "anidadas", "en", "el", "ordenador"]

menu = """
+---------------------------+
|   1. Count                |
|   2. Replace              |
|   3. Delate               |
|   4. List                 |
|   5. Exit                 |
+---------------------------+
"""
aux = True
while (aux):
    print(menu)
    p = input("Elige un numero: ")
    while p.isdigit() == False or int(p) > 5:
        print(menu)
        p = input("Error, introduce un numero del menu: ")
    int(p)
    # Caso 1
    if int(p) == 1:
        texto = input("Introduce un texto: ").lower()
        if texto in lista:
            print("La cadena aparece ", lista.count(texto), "vez/veces en la lista")
        else:
            print("No se ha encontrado de valor introducido.")

    # Caso 2
    if int(p) == 2:
        text = input("Introduce un texto: ").lower()
        if text in lista:
            remp = input("Introduce un texto para reemplazar: ")
            lista = [i.replace(text, remp) for i in lista]
        else:
            print("No se ha encontrado de valor introducido.")

    # Caso 3
    if int(p) == 3:
        valor3 = input("Introduce un string para borrar: ").lower()
        if valor3 in lista:
            for j in lista:
                if j == valor3:
                    lista.remove(j)
        else:
            print("No se ha encontrado de valor introducido.")
    # Caso 4
    if int(p) == 4:
        print(*lista)

    # Caso 5
    if int(p) == 5:
        exit()
