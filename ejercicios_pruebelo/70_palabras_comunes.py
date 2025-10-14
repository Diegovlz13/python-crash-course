
from pathlib import Path

filename = '/Users/diegovelazquez/Documents/python_crash_course/apuntes/books/alice.txt'

try: 
    path = Path(filename)
    contents = path.read_text()
except:
    pass
else:
    print(contents.lower().count('shower'))