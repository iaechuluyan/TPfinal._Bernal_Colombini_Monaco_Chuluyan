import unittest
import numpy as np
from read_txt_files import get_frequency

class TestGetFrequency(unittest.TestCase):
    def test_array_argument(self):
        arg1 = np.array([1,2,3,4])
        self.assertRaises(TypeError,get_frequency,arg1)

    def test_none_argument(self):
        arg1 = None
        self.assertRaises(TypeError,get_frequency,arg1)
    
    def test_string_argument(self):
        arg1 = "[1,2,3]"
        self.assertRaises(ValueError,get_frequency,arg1)

    def test_int_argument(self):
        arg1 = 10
        self.assertRaises(TypeError,get_frequency,arg1)
    
    def test_float_argument(self):
        arg1 = 10.10
        self.assertRaises(TypeError,get_frequency,arg1)

    def test_list(self):
        test1 = get_frequency("A4")
        test2 = 440.0
        self.assertEqual(test1,test2)

if __name__ == '__main__':
    unittest.main()