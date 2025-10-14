from random import choice
from time import sleep

CARACTERES = ('1', '2', '3', '4', '5', '6', '7', 
              '8', '9', '0', 'A', 'B', 'C', 'D', 'E')

def seleccionar(caracteres, combinacion = ""):
    """Selecciona 4 caracteres aleatoriamente de la lista y los devuelve."""
    for _ in range(5):
        combinacion += choice(caracteres)
    return combinacion

def comprobar_mi_boleto(mi_boleto):
    """Comprueba cuántas véces le tomo al programa, que yo ganará."""
    contador = 0
    while True:
        contador += 1
        boleto_premiado = seleccionar(CARACTERES)
        if mi_boleto == boleto_premiado:
            break
    return contador
            

# Escogiendo mi combinación favorita
mi_boleto = "D1360"
ejecuciones = comprobar_mi_boleto(mi_boleto)
print(f"Le tomo {ejecuciones} ejecuciones al programa obtener boleto: {mi_boleto}")