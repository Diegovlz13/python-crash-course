glosario = {
    'entero': 'Número sin decimales',
    'float': 'Número con decimales',
    'string': 'Conjunto de caracteres',
    'lista': 'Conjunto de elementos separados por comas y entre []',
    'variable': 'Dirección de memoria que apunta a un valor almacenado',
    'diccionario': 'Colección de pares clave:valor encerrada en {}',
    'booleano': 'Tipo de dato lógico que puede ser True o False',
    'funcion': 'Bloque de código que se ejecuta cuando es llamado',
    'bucle': 'Estructura que repite un bloque de código mientras se cumpla una condición',
    'clase': 'Plantilla para crear objetos que agrupa atributos y métodos'
}

print("Definiciones:")
for key, value in glosario.items():
    print(f"- {key.title()}: {value}.")