current_users = ['diego', 'yunuen', 'samantha', 'matias', 'osvaldo']
new_users = ['naomi', 'santiago', 'DIEGo', 'MAtias', 'Africa']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Ingrese otro nombre {new_user.lower()}, este ya esta ocupado.")
    else:
        print(f"{new_user.lower()}, este nombre de usuario esta disponible.")
