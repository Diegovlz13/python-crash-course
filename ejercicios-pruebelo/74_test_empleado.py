import unittest
from empleado import Empleado

class TestEmpleado(unittest.TestCase):
    """Pruebas para la clase Empleado."""
    
    def setUp(self):
        """Crea un empleado."""
        self.empleado = Empleado('Naomi', 'Rodriguez', 10_000)
        
    def test_dar_aumento_predeterminado(self):
        """Incrementa el salario del empleado con el valor predeterminado de 5_000 euros."""
        self.empleado.dar_aumento()
        self.assertEqual(self.empleado.salario_anual, 15_000)
    
    def test_dar_aumento_personalizado(self):
        """Incrementa el salario del empleado segun lo dado."""
        self.empleado.dar_aumento(10_000)
        self.assertEqual(self.empleado.salario_anual, 20_000)
        
if __name__ == '__main__':
    unittest.main()
        