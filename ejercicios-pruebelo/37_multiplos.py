numero = int(input("Dame un número entero y te diré si es multiplo de 10: "))

if numero % 10 == 0:
    print(f"El número {numero} SI es multiplo de 10.")
else:
    print(f"El número {numero} NO es multiplo de 10.")