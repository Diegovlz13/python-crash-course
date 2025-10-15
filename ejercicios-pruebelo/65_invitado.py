from pathlib import Path

content = input('Ingresa tu nombre: ')
content = f"{content}\n"

path = Path('invitado.txt')
path.write_text(content)