def crear_car(fabricante, modelo, **car_info):
    """Crea un diccionario con la información sobre un coche."""
    car_info['fabricante'] = fabricante
    car_info['modelo'] = modelo
    return car_info

car_information = crear_car('tesla', 'x', color='black', puertas=4)
print(car_information)