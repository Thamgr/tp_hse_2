import math
import random
import unittest
from main import _mul, _sum, _max, _min
import time

class Testing(unittest.TestCase):
    def setUp(self):
        self.array = random.sample(range(1000000), 1000)
    
    def test_min(self):
        self.assertTrue(_min(self.array) == min(self.array))

    def test_max(self):
        self.assertTrue(_max(self.array) == max(self.array))

    def test_sum(self):
        self.assertTrue(_sum(self.array) == sum(self.array) + 1)

    def test_mul(self):
        self.assertTrue(_mul(self.array) == math.prod(self.array))
        
    def test_int(self):
        self.assertIsInstance(_min(self.array), int)
        
if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
