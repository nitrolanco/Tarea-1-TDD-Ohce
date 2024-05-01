import unittest
import functions 
import datetime

class TestStringMethods(unittest.TestCase):
     
    def test_detect_palindrome(self, word = "vaca"):
        current_hour = datetime.datetime.now().hour

        if word == word[::-1]:
            expected_string = "¡Bonita palabra!"
        else:
            expected_string = word[::-1]
        try:
            self.assertEqual(functions.handle_word(word), expected_string)
            print("test approved, assertion passed")
        except AssertionError as e:
            print(f"Test for word '{word}' failed: {e}")

if __name__ == '__main__':
    words = ["hola", "vaca", "oso"]
    for word in words:
        TestStringMethods().test_detect_palindrome(word)