def make_pizza(size, *toppings):
    """Resumen la pizza que estamos apunto de hacer."""
    print(f"\nMaking a {size}-inch pizza with the followings toppings:")
    for topping in toppings:
        print(f"- {topping}")