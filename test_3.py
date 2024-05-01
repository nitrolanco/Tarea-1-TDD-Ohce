import unittest
import functions

class TestStringMethods(unittest.TestCase):
     
    def test_stop(self, name = "Anibal"):
    
        self.assertEqual(functions.handle_stop(), f"Adios {name}!")

if __name__ == '__main__':
    unittest.main()