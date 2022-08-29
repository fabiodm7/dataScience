import unittest
from city_functions import get_cidade_pais

class NamesTestCase(unittest.TestCase):
    """Teste para cidade_pais"""

    def test_city_country(self):
        """Santiago, Chile funciona"""
        capital_pais = get_cidade_pais('santiago','chile')
        self.assertEqual(capital_pais,'Santiago, Chile')

    def test_city_country_population(self):
        """Santiago, Chile funciona"""
        capital_pais = get_cidade_pais('santiago','chile',500000)
        self.assertEqual(capital_pais,'Santiago, Chile - População: 500000.')

unittest.main()