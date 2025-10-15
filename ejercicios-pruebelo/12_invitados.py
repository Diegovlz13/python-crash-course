invitados = ["Elon Musk", "Aristoteles", "Messi"]

print(f"{invitados[0]}, te invito a cenar.")
print(f"{invitados[1]}, te invito a cenar.")
print(f"{invitados[2]}, te invito a cenar.")
print(f"{invitados[0]} no podrá asistir.")

# Lista actualizada
invitados[0] = "Tyler Joseph"
print(f"{invitados[0]}, te invito a cenar.")
print(f"{invitados[1]}, te invito a cenar.")
print(f"{invitados[2]}, te invito a cenar.")

# Nueva actualizacion, mas invitados
print("Se encontro una mesa mas grande, vendran mas invitados.")
invitados.insert(0, "Roberto Martinez")
invitados.insert(3, "Steve Jobs")
invitados.insert(5, "Chespirito")

# Lista actualizada
print(f"{invitados[0]}, te invito a cenar.")
print(f"{invitados[1]}, te invito a cenar.")
print(f"{invitados[2]}, te invito a cenar.")
print(f"{invitados[3]}, te invito a cenar.")
print(f"{invitados[4]}, te invito a cenar.")
print(f"{invitados[5]}, te invito a cenar.")

# La mesa no llego, solo hay espacio para dos personas
print(f"{invitados.pop()}, lo siento, no podré invitarte a cenar.")
print(f"{invitados.pop()}, lo siento, no podré invitarte a cenar.")
print(f"{invitados.pop()}, lo siento, no podré invitarte a cenar.")
print(f"{invitados.pop()}, lo siento, no podré invitarte a cenar.")

# Mensaje de bienvenida a las personas invitadas
print("El total de invitados son:", len(invitados))
print(f"{invitados[0]}, la invitación sigue en pie.")
print(f"{invitados[1]}, la invitación sigue en pie.")

# Dejando la lista vacia
del invitados[0]
del invitados[0]
print(invitados)