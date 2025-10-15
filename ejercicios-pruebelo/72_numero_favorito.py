from pathlib import Path
import json


def obtener_numero_almacenado(path):
    """Busca si existe un registro de un número favorito."""
    if path.exists():
        contenido = path.read_text()
        numero = json.loads(contenido)
        return numero
    else:
        return None

def obtener_nuevo_numero(path):
    """Solicita su numero favorito al usuario y lo guarda."""
    numero = input("¿Cuál es tu número favorito? ")
    contenido = json.dumps(numero)
    path.write_text(contenido)
    return numero

def mostrar_numero_favorito():
    """Muestra al usuario su número favorito, si no hay registro lo menciona."""
    path = Path('favorite_number.json')
    numero = obtener_numero_almacenado(path)
    if numero:
        print(f"Conozco tu número favorito, es {numero}.")
    else:
        numero = obtener_nuevo_numero(path)
        print("Lo recordaré para la proxima vez.")
        
        
mostrar_numero_favorito()







