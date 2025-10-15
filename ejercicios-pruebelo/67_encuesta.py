from pathlib import Path

path = Path('encuesta.txt')

content = ""
continuar = ""
while continuar != 's':
    name = input('Ingresa tu nombre: ')
    motive = input('¿Por que te gusta programar? ')
    print(f"{name}, gracias por responder la encuesta.")
    content += f"{name}, {motive}\n"
    path.write_text(content)
    continuar = input('Presiona cualquier tecla para continuar o (s) para salir: ').lower()
    print("")