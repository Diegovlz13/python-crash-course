def build_person(first_name, last_name, age=None):
    """Devuelve un diccionario de información sobre una persona."""
    person = {'first_name': first_name, 'last_name': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('tyler', 'joseph', 33)
print(musician)