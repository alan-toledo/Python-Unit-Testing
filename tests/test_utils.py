import unittest
from utils import get_max, get_min, get_avg

class TestGetMax(unittest.TestCase):
    def test_get_max_value_10(self):
        self.assertEqual(get_max([1,2,10]), 10)

class TestGetMin(unittest.TestCase):
    def test_get_min_value_1(self):
        self.assertEqual(get_min([1,2,10]), 1)

class TestGetAvg(unittest.TestCase):
    def test_get_avg_value_2(self):
        self.assertEqual(get_avg([1,2,3]), 2)
