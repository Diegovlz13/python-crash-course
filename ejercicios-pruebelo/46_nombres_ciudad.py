def ciudad_pais(ciudad, pais):
    """Retorna la ciudad y pais en un formato adecuado."""
    return f"{ciudad.title()}, {pais.title()}"


# Llamada 1
lugar1 = ciudad_pais('guadalajara', 'mexico')
print(lugar1)
# Llamada 2
lugar1 = ciudad_pais('monterrey', 'mexico')
print(lugar1)
# Llamada 3
lugar1 = ciudad_pais('ciudad de mexico', 'mexico')
print(lugar1)