import unittest
from ciudad_funciones import get_formatted_city_country

class CityCountryTestCase(unittest.TestCase):
    """Pruebas para 'ciudad_funciones'."""
    
    def test_city_country(self):
        """¿Funcionan lugares como 'Santiago, Chile'?"""
        formatted_place = get_formatted_city_country('santiago', 'chile')
        self.assertEqual(formatted_place, 'Santiago, Chile')
        
    def test_city_country_population(self):
        """¿Funcionan lugares como 'Santiago, Chile - population 5000000'?"""
        formatted_place = get_formatted_city_country(
            'santiago', 'chile', 5_000_000)
        self.assertEqual(formatted_place, 'Santiago, Chile - population 5000000')
        
        
if __name__ == '__main__':
    unittest.main()