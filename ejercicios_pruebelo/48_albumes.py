def hacer_album(nombre_artista, titulo_album, numero_canciones=None):
    """Retorna un diccionario que guarda la información de un album musical."""
    album = {'nombre_artista': nombre_artista, 'titulo_album': titulo_album}
    if numero_canciones:
        album['numero_canciones'] = numero_canciones
    return album
    
continuar = "si"
while continuar == "si":
    artista = input('Dame el nombre del artista: ')
    titulo = input('Dame el título del albúm: ')
    num_canciones = int(input('¿Cuántas canciones tiene el albúm? '))
    
    album = hacer_album(nombre_artista=artista, titulo_album=titulo, numero_canciones=num_canciones)
    print(album)
    
    continuar = input('¿Deseas crear otro album? (si/no): ').lower()