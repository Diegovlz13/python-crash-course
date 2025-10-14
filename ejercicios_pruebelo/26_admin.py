users = []

if users:
    for user in users:
        if user == 'admin':
            print("Hola, admin, ¿quieres ver un informe de estado?")
        else:
            print(f"Hola, {user}, gracias por volver a entrar")
else:
    print("¡Necesitamos encontrar algún usuario!")