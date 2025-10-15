pedidos_bocadillos = [
    'nachos con queso',
    'mini hamburguesas',
    'alitas de pollo BBQ',
    'rollitos primavera',
    'palitos de mozzarella',
    'aros de cebolla',
    'nachos con queso',
    'papas fritas con cheddar y tocino',
    'guacamole con totopos',
    'bruschetta de tomate y albahaca',
    'nachos con queso',
    'bolitas de risotto'
]

bocadillos_terminados = []

print("\n--- Preparando bocadillos ---")
while pedidos_bocadillos:
    bocadillo_pedido = pedidos_bocadillos.pop()
    # Ya no quedan nachos con queso
    if bocadillo_pedido == 'nachos con queso':
        print("* Ya no quedan nachos con queso.")
    else:
        print(f"* Su bocadillo de {bocadillo_pedido} está listo.")
        bocadillos_terminados.append(bocadillo_pedido)
    
print("\n--- Bocadillos hechos ---")
contador = 0
while contador < len(bocadillos_terminados):
    print(f"{contador + 1}. {bocadillos_terminados[contador].capitalize()}.")
    contador += 1