# Guarda la información sobre una pizza que se está pidiendo.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

# Resume el pedido
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")