def describe_pet(pet_name, animal_type='dog'):
    """Muestra información sobre una mascota."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
    
describe_pet(pet_name='africa')
describe_pet(pet_name='harry', animal_type='hamster')