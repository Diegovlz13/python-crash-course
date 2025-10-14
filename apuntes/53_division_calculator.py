print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input('\nFirst number: ')
    if first_number == 'q':
        break
    second_number = input('\nSecond number: ')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("\nTu segundo numero no puede ser cero.")
    else:
        print(f"\nResultado = {answer}")
    