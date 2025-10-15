person1 = {
    'nombre': 'naomi',
    'apellido': 'rodriguez',
    'edad': 22,
    'ciudad': 'guadalajara'
}

person2 = {
    'nombre': 'santiago',
    'apellido': 'robledo',
    'edad': 14,
    'ciudad': 'guadalajara'  
}

person3 = {
    'nombre': 'xitlalli',
    'apellido': 'rodriguez',
    'edad': 19,
    'ciudad': 'guadalajara'  
}

people = [person1, person2, person3]

print("Datos sobre las personas:")
for person in people:
    for clave, valor in person.items():
        if type(valor) == str:
            print(f"{clave.title()}: {valor.title()}")
        else:
            print(f"{clave.title()}: {valor}")
    print("----------------------")
    