def hacer_emparedado(*args):
    print("Resumen del sandwich:")
    for arg in args:
        print(f"- {arg}")
        
hacer_emparedado('Lleva jitomate y cebolla', 'Lleva jamón de pavo')
hacer_emparedado('Debe estar tostado', 'Sin aguacate')
hacer_emparedado('Lleva pollo', 'Sin aderezo', 'Con mucha lechuga')