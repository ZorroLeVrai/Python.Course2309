import unittest
from fizzbuzz2 import fizz_buzz, fizz_buzz2, create_fb_list

class TestFizzBuzz(unittest.TestCase):

    def test_fizzBuzz(self):
        self.assertEqual(fizz_buzz2(3), "Fizz")
        self.assertEqual(fizz_buzz2(5), "Buzz")
        self.assertEqual(fizz_buzz2(15), "FizzBuzz")
        self.assertEqual(fizz_buzz2(28), 28)

    def test_fizzBuzz(self):
        self.assertEqual(create_fb_list(2,4), [2, "Fizz", 4])

if __name__ == "__main__":
    unittest.main()