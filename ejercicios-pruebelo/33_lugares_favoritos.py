lugares_favoritos = {
    'naomi': ['grecia', 'españa', 'francia'],
    'diego': ['china', 'japan', 'finlandia'],
    'carlos': ['suiza', 'alemania', 'usa']
}

for nombre, lugares in lugares_favoritos.items():
    print(f"{nombre.title()}, tus lugares favoritos son:")
    for lugar in lugares:
        print(f"- {lugar.title()}")