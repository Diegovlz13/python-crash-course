ingrediente = ""
prompt = "¿Que ingrediente desea agregar a su pizza?\n-> Escriba (quit) para salir: "
while ingrediente != 'quit':
    ingrediente = input(prompt)
    if ingrediente != 'quit':
        print(f"Se añadio {ingrediente.title()} correctamente.")
    else:
        print("¡Hasta luego!")    