
from pathlib import Path

# Perros
try:
    path = Path('perros.txt')
    contents = path.read_text()
except FileNotFoundError:
    pass
else:
    print(contents)
    
# Gatos
try:
    path = Path('gatos.txt')
    contents = path.read_text()
except FileNotFoundError:
    pass
else:
    print(contents)
