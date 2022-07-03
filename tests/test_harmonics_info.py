import unittest
import numpy as np
from read_txt_files import harmonics_info

class TestHarmonicsInfo(unittest.TestCase):
    def test_array_argument(self):
        arg1 = np.array([1,2,3,4])
        self.assertRaises(TypeError,harmonics_info,arg1)

    def test_none_argument(self):
        arg1 = None
        self.assertRaises(TypeError,harmonics_info,arg1)
    
    def test_string_argument(self):
        arg1 = "[1,2,3]"
        self.assertRaises(TypeError,harmonics_info,arg1)

    def test_int_argument(self):
        arg1 = 10
        self.assertRaises(TypeError,harmonics_info,arg1)
    
    def test_float_argument(self):
        arg1 = 10.10
        self.assertRaises(ValueError,harmonics_info,arg1)

    def test_list(self):
        test1 = harmonics_info("test_file_harmonics.txt")
        test2 = [[['1', '1'], ['2', '0.72727272'], ['3', '0.32323232'], ['4', '0.151515151']], [['LINEAR', '0.2'], ['CONSTANT'], ['INVLINEAR', '0.4']]]
        self.assertEqual(test1,test2)

if __name__ == '__main__':
    unittest.main()