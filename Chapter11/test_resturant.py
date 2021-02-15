#print("-----------------------------------Hands On #2------------------------------------------")
import unittest

from resturant import Restaurant

class TestRestuarant(unittest.TestCase):
    """Tests imported resturant"""
#used sales numbers from example as number served 
    def setUp(self):
        """Test case Resturant setup"""
        name = "Stella Tattorili"
        cuisine_type = "French"
        number_served = 15000
        self.resturant = Restaurant(name, cuisine_type, number_served)
      
    def test_set_number_served(self):
        """Tests number served"""
        served = 100000
        self.resturant.set_number_served(served)
        self.assertEqual(self.resturant.number_served, 100000)   
   
    def test_increment_number_served(self):
        """Tests incremented number served"""
        served = 200
        self.resturant.increment_number_served(served)
        self.assertEqual(self.resturant.number_served, 15200)  

    def test_increment_number_served_string(self):
        served="100"
        self.resturant.increment_number_served(served)
        self.assertEqual(self.resturant.number_served, 15100) 

if __name__ == '__main__':
    unittest.main()
