import unittest
import numpy as np
from sorting import sorting_harmonics

class TestSortingHarmonics(unittest.TestCase):
    def test_array_argument(self):
        arg1 = np.array([1,2,3,4])
        self.assertRaises(TypeError,sorting_harmonics,arg1)

    def test_none_argument(self):
        arg1 = None
        self.assertRaises(TypeError,sorting_harmonics,arg1)
    
    def test_string_argument(self):
        arg1 = "[1,2,3]"
        self.assertRaises(TypeError,sorting_harmonics,arg1)

    def test_int_argument(self):
        arg1 = 10
        self.assertRaises(TypeError,sorting_harmonics,arg1)
    
    def test_float_argument(self):
        arg1 = 10.10
        self.assertRaises(TypeError,sorting_harmonics,arg1)

    def test_list(self):
        test1 = sorting_harmonics([[['4', '0.151515151'], ['1', '1'], ['3', '0.32323232'], ['2', '0.72727272']]])
        test2 = [[['4', '0.151515151'], ['1', '1'], ['3', '0.32323232'], ['2', '0.72727272']]]
        self.assertEqual(test1,test2)

if __name__ == '__main__':
    unittest.main()