mascota1 = {
    'nombre': 'africa',
    'dueño': 'diego'
}

mascota2 = {
    'nombre': 'gordo',
    'dueño': 'naomi'  
}

mascota3 = {
    'nombre': 'frederick',
    'dueño': 'jeshua'
}

mascotas = [mascota1, mascota2, mascota3]

print("Datos sobre las mascotas:")
for mascota in mascotas:
    for clave, valor in mascota.items():
        print(f"{clave.title()}: {valor.title()}")
    print("----------------------")
    