def hacer_album(nombre_artista, titulo_album, numero_canciones=None):
    """Retorna un diccionario que guarda la información de un album musical."""
    album = {'nombre_artista': nombre_artista, 'titulo_album': titulo_album}
    if numero_canciones:
        album['numero_canciones'] = numero_canciones
    return album
    
    
# Llamada 1.
album1 = hacer_album('michael jackson', 'triller', 30)
# Llamada 2.
album2 = hacer_album('twenty one pilots', 'clancy')
# Llamada 3.
album3 = hacer_album('twenty one pilots', 'breach', 13)

# Mostrando resultados.
print(album1)
print(album2)
print(album3)