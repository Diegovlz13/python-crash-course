import unittest
from function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Pruebas para 'function.py'."""
    
    def test_first_last_name(self):
        """¿Funcionan nombres como 'Diego Velazquez'?"""
        formatted_name = get_formatted_name('diego', 'velazquez')
        self.assertEqual(formatted_name, 'Diego Velazquez')
        
    def test_first_last_middle_name(self):
        """¿Funcionan nombres como 'Diego Osvaldo Velazquez''"""
        formatted_name = get_formatted_name(
            'diego', 'velazquez', 'osvaldo')
        self.assertEqual(formatted_name, 'Diego Osvaldo Velazquez')
        
if __name__ == '__main__':
    unittest.main()