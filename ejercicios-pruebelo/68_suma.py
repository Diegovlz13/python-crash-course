
def solicitar_numeros():
    """Solicita dos números al usuario, también se asegura de que son valores númericos y al final los retorna."""
    while True:
        try:
            num1 = float(input('Dame el primer número: '))
        except ValueError:
            print("Debes ingresar un número.\n")
        else:
            break  
    while True:
        try:
            num2 = float(input('Dame el segundo número: '))
        except ValueError:
            print("Debes ingresar un número.\n")
        else:
            break 
    return num1, num2


def sumar(num1, num2):
    """Devuelve la suma de dos números."""
    return num1 + num2


num1, num2 = solicitar_numeros()
resultado = sumar(num1, num2)
print(f"El resultado es {resultado}")