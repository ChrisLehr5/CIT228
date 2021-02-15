#print("-----------------------------------Hands On #2, Exercise 11-3------------------------------------------")
import unittest

from employee import Employee 

class TestEmployee(unittest.TestCase):
    """Tests imported employee"""

    def setUp(self):
        """Test case employee setup"""
        self.christine = Employee('christine', 'lehr', 50000)

    def test_give_default_raise(self):
        """Tests that default raise is working"""
        self.christine.give_raise()
        self.assertEqual(self.christine.salary, 55000)

    def test_give_custom_raise(self):
        """Tests that custom raise is working"""
        self.christine.give_raise(100000)
        self.assertEqual(self.christine.salary, 150000)

if __name__ == '__main__':
    unittest.main()