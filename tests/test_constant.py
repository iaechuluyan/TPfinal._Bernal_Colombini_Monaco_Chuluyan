import unittest
import numpy as np
from a_s_d_functions import Functions

object_test = Functions()

class TestConstant(unittest.TestCase):
    def test_none_argument(self):
        arg1 = None
        self.assertRaises(TypeError,object_test.constant,arg1)
    
    def test_empty_array_argument(self):
        arg1 = np.array([])
        self.assertRaises(ValueError,object_test.constant,arg1)
    
    def test_string_argument(self):
        arg1 = "[1,2,3]"
        self.assertRaises(TypeError,object_test.constant,arg1)

    def test_int_argument(self):
        arg1 = 10
        self.assertRaises(TypeError,object_test.constant,arg1)
    
    def test_float_argument(self):
        arg1 = 10.10
        self.assertRaises(TypeError,object_test.constant,arg1)
    
    def test_array(self):
        array_test1 = object_test.constant(np.array([4,2,3]))
        array_test2 = np.array([1.,1.,1.])
        self.assertAlmostEqual(array_test1.all(),array_test2.all())

if __name__ == '__main__':
    unittest.main()
    