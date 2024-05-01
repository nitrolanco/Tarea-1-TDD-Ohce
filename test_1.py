import unittest
import functions 
import datetime

class TestStringMethods(unittest.TestCase):
     
    def test_welcome(self, name_ohce=None):  # Accept an optional argument for name_ohce
        if name_ohce is None:
            name_ohce = "Anibal" 
        current_hour = datetime.datetime.now().hour
        if 20 <= current_hour < 24 or 0 <= current_hour < 6:
            expected_string = f'¡Buenas noches {name_ohce}!'
        elif 6 <= current_hour < 12:
            expected_string = f'¡Buenos días {name_ohce}!'
        elif 12 <= current_hour < 20:
            expected_string = f'¡Buenas tardes {name_ohce}!'
        self.assertEqual(functions.welcome(name_ohce), expected_string)

if __name__ == '__main__':
    unittest.main()