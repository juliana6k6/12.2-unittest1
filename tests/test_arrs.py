import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")
        self.assertEqual(arrs.get([3, 4, 5, 6], 5, "test"), "test")
        self.assertEqual(arrs.get([3, 4, 5, 6], 0, "test"), 3)

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 0, 5), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 2, 5), [3])
        self.assertEqual(arrs.my_slice([], 2, 5), [])
        self.assertEqual(arrs.my_slice([1, 2, 3], None, 2), [1, 2])
