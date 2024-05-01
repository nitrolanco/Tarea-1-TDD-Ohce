import unittest
import functions


class TestStringMethods(unittest.TestCase):
    def test_stop(self, name="Anibal"):
        expected_output = f"""{functions.welcome(name)}
{functions.handle_word("hola")}
{functions.handle_word("vaca")}
{functions.handle_word("oso")}
{functions.handle_stop(name)}"""
        self.assertEqual(
            functions.main_loop(name, "hola", "vaca", "oso", "stop!"), expected_output
        )


if __name__ == "__main__":
    unittest.main()
