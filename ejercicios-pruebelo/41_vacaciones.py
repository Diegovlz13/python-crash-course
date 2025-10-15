responses = {}

polling_active = True

while polling_active:
    name = input("\n¿Cuál es tu nombre? ")
    response = input("Si pudieras visitar cualquier parte del mundo, ¿dónde irías? ")
    
    responses[name] = response
    
    repeat = input("¿Otra persona responderá la encuesta? (si/no): ")
    if repeat == 'no':
        polling_active = False
        
print("\n--- Resultados encuesta ---")
for name, response in responses.items():
    print(f"{name.title()} le gustaría ir a {response.title()}.")
    