from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
lines = contents.splitlines()

print(f"Contenido viejo:")
for line in lines:
    print(line)

print("Contenido nuevo:")
for line in lines:
    line = line.replace('Python', 'C')
    print(line)