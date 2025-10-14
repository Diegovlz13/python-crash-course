responses = {}

# Configura una bandera para indicar que la encuesta está activa.
polling_active = True

while polling_active:
    # Pide el nombre y la respuesta de la persona.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    # Guarda la respuesta en un diccionario
    responses[name] = response
    
    # Averigua si alguien más va a hacer la encuesta.
    repeat = input("Would you like to let another person respond? (yes/no): ")
    if repeat == 'no':
        polling_active = False
        
# La encuesta está completa. Muestra los resultados.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response}.")
    