def describir_ciudad(ciudad, pais='mexico'):
    """
    Describe a que pais pertenece una ciudad.
    
    Argumentos
        ciudad (posicional): Nombre de la ciudad.
        pais (por defecto - mexico): Nombre del pais.
    """
    print(f"{ciudad.title()} esta en {pais.title()}.")
    

describir_ciudad(ciudad='guadalajara')
describir_ciudad(ciudad='monterrey')
describir_ciudad(ciudad='new york', pais='usa')