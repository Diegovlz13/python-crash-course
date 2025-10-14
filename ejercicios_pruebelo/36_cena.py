cantidad_personas = int(input("¿Cuántas personas vendrán a la cena? "))

if cantidad_personas > 8:
    print(f"Debido a que son {cantidad_personas}, tendrán que esperar una mesa.")
else:
    print(f"Su mesa para {cantidad_personas} ya esta lista.")