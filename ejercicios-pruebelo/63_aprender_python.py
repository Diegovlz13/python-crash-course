from pathlib import Path

print("Leyendo todo el archivo...")
path = Path('learning_python.txt')
contents = path.read_text()
print(contents)

print("Leyendo mediante un bucle...")
lines = contents.splitlines()
for line in lines:
    print(line)

print("Trabajando con la lista fuera...")
final_line = str(lines[-1])
print(final_line)