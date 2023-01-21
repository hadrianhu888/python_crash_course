import unittest
from name_function_practice import *

class NamesTestCase(unittest.TestCase):
    """Test for 'name_function_practice.py'"""
    
    def test_first_name_practice(self):
        """Do names like Janis Joplin work?"""
        first = 'janis'
        last = 'joplin'        
        formatted_name = get_formatted_name_practice(first,last)
        formatted_expected = f"{first} {last}".title()        
        self.assertEqual(formatted_name,formatted_expected)
    
    def test_full_name_extended_practice(self):
        """Does names like Xinyu Hadrian Hu work?"""
        first = 'xinyu'
        middle = 'hadrian'
        last = 'hu'
        formatted_name = get_formatted_name_practice_extended(first,middle,last)
        formatted_expected = f"{first} {middle} {last}".title()
        self.assertEqual(formatted_name,formatted_expected)
        
if __name__ == '__main__':
    unittest.main()

