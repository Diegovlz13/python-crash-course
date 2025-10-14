# Hace una lista vacia para guardar aliens.
aliens = []

# Hace 30 aliens verdes.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    
# Cambia los tres primeros aliens
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    
# Muestra los 5 primeros aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Muestra cuántos aliens se han creado.
print(f"Total number of aliens: {len(aliens)}")
