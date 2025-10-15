pizzas = ['carnes frias', 'cuatro quesos', 'pepperoni']
friend_pizzas = pizzas[:]

pizzas.append('margarita')
friend_pizzas.append('italiana')

print("Mis pizzas favoritas son:")
for pizza in pizzas:
    print(pizza)

print("Las favoritas de mi amigo son:")
for pizza in friend_pizzas:
    print(pizza)