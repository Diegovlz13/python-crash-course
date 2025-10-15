from random import randint as rd

class Dado:
    """Simula la creación de un dado."""
    
    def __init__(self, caras=6):
        """Inicializa los atributos de la clase."""
        self.caras = caras
        
    def tirar_dado(self):
        """Simula el lanzamiento de un dado, devolviendo el número obtenido."""
        return rd(1, self.caras)
    
def main():
    """Cuerpo principal del programa."""
    
    dado = Dado(20) # Por defecto tiene 6 caras
    
    print("Lanzamientos (20 caras)")
    for i in range(10):
        print(f"#{i+1} -> {dado.tirar_dado()}")
    

if __name__ == '__main__':
    main()       