def build_profile(first, last, **user_info):
    """Crea un diccionario con todo lo que sabemos sobre un usuario."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('diego', 'velazquez',
                             location='cucei',
                             field='informatica',
                             semester=6,
                             age=22)

print(user_profile)