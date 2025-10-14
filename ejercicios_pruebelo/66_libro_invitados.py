from pathlib import Path

path = Path('libro_invitados.txt')

content = ""
while True:
    print("Escribe (salir) para terminar el programa.")
    name = input('Ingresa tu nombre: ')
    if name == 'salir':
        break
    else:
        print(f"Hola, {name}, gracias por utilizar el programa.\n")
        content += f"{name}, ingreso al sistema\n"
        path.write_text(content)
        