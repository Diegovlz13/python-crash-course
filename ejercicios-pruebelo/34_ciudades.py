ciudades = {
    'china': {
        'pais': 'china',
        'poblacion': 1416,
        'curiosidad': 'Tiene el sistema ferroviario de alta velocidad más '
        'extenso del mundo, conectando numerosas grandes ciudades con trenes '
        'que alcanzan velocidades de hasta 350 km/h',   
    }, 
    'usa': {
        'pais': 'Estados Unidos de America',
        'poblacion': 347,
        'curiosidad': 'Mientras que sea el tercer país más poblado, también presenta '
        'una enorme diversidad de ecosistemas — desde las tundras árticas en Alaska '
        'hasta desiertos, bosques tropicales y grandes llanuras. (Si quieres, te doy '
        'una curiosidad más concreta de EEUU)',  
    },
    'rusia': {
        'pais': 'rusia',
        'poblacion': 146,
        'curiosidad': 'Es el país más grande del mundo por superficie, abarcando '
        '11 husos horarios diferentes'
    }
}

for ciudad, ciudad_info in ciudades.items():
    print(f"La información de {ciudad.title()} es la siguiente:")
    for clave, valor in ciudad_info.items():
        if type(valor) == str:
           print(f"{clave.title()}: {valor}.")
        else:
            print(f"{clave.title()}: {valor} millones de personas.")
    print("")