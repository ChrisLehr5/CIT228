import unittest

from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_function.py"""
    def test_city_country(self):
        """Does city, country work?"""
        santiago_chile = city_country('santiago', 'chile')
        self.assertEqual(santiago_chile, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()