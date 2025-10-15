def hacer_camiseta(talla='L', leyenda='Me encanta Python'):
    """
    Imprime un estampado en la camiseta.
    
    Argumentos
        talla: Talla de la camiseta.
        leyenda: Frase impresa en la camiseta.
        
    Retorna
        None
    """
    print(f'La talla de la camiseta es {talla} y su estampado dice "{leyenda}".')
    

# Creación de camisetas.
hacer_camiseta()
hacer_camiseta(talla='M')
hacer_camiseta(talla='X', leyenda='No subo gordas')