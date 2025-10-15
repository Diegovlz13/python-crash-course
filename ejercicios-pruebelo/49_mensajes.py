
def enviar_mensajes(mensajes, mensajes_enviados):
    while mensajes:
        mensaje = mensajes.pop()
        print(mensaje)
        mensajes_enviados.append(mensaje)


mensajes = ['hola', '¿cómo estas', '¿ya llegaste?', 'te amo']
mensajes_enviados = []

enviar_mensajes(mensajes[:], mensajes_enviados)
print(f"Mensajes: {mensajes}")
print(f"Mensajes enviados: {mensajes_enviados}")