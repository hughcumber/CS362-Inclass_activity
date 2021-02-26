import unittest
import math
import fibonacci
import fact
import pytest

class TestFib(unittest.TestCase):

    def test_fibonaci(self):
        self.assertEqual(fibonacci_index(5), 6);

    def test_fibonaci(self):
        self.assertEqual(fibonacci_index(2), 4);

    def test_fibonaci(self):
        self.assertEqual(fibonacci_index(21), 9);


class TestFact(unittest.TestCase):

    def test_fact(self):
        self.assertEqual(fact(6), 720);

    def test_fact(self):
        self.assertEqual(fact(5), 120);

    def test_fact(self):
        self.assertEqual(fact(0), 1);










if __name__ == '__main__':
    unittest.main()
