def formatear_nombre(nombre, apellido):
    nombre_completo = f"{nombre} {apellido}"
    return nombre_completo.title()


nombre = formatear_nombre('diego osvaldo', 'de la cruz VElazquez')
print(nombre)    