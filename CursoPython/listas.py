friend = ["Kevin", "Karen", "Jim", "Ana", "Kevins", "Jimie", "Paloma"]
lucky_number = [4, 8, 15, 16, 23, 42]
# print(friend[1:3])
# friend.extend(lucky_number) #Concatenar arrays
friend.append("Oliver")  # Añadir valores
friend.insert(1, "oh")  # reemplazar
print(friend)
# Eliminar valores
friend.remove("oh")
print(friend)
# Pop -> Elimina el ultimo elemento
friend.pop()

print(friend)

print(friend.count("Kevins"))

friend.sort()

lucky_number.sort()

print(friend)

print(lucky_number)

lucky_number.reverse()

print(lucky_number)

frinds2 = friend.copy()

# Tople

coordenadas = (4, 5) #No s epueden modificar, let
