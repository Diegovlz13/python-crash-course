def print_models(unprinted_desings, completed_models):
    """
    Simula imprimir cada diseño, hasta que no queda ninguno.
    Mueve cada diseño a completed_models después de la impresión.
    """
    while unprinted_desings:
        current_desing = unprinted_desings.pop()
        print(f"Printing model: {current_desing}")
        completed_models.append(current_desing)

def show_completed_models(completed_models):
    """Muestra todos los modelos que se han imprimido."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
        

unprinted_desings = ['phone case', 'robot pendant', 'dodecahedronk']
completed_models = []
print_models(unprinted_desings, completed_models)
show_completed_models(completed_models)
print(unprinted_desings)