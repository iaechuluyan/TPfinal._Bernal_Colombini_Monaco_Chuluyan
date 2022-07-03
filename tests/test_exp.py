import unittest
import numpy as np
from a_s_d_functions import Functions

object_test = Functions()

class TestExp(unittest.TestCase):
    def test_empty_array_argument(self):
        arg1 = np.array([])
        arg2 = 2
        arg3 = np.array([1,2,3])
        self.assertRaises(ValueError,object_test.exp,arg1,arg2) #rari!!!
        self.assertRaises(TypeError,object_test.exp,arg3,arg1)

    def test_none_argument(self):
        arg1 = None
        arg2 = 2
        arg3 = np.array([1,2,3])
        self.assertRaises(TypeError,object_test.exp,arg1,arg2)
        self.assertRaises(TypeError,object_test.exp,arg3,arg1)
    
    def test_string_argument(self):
        arg1 = "[1,2,3]"
        arg2 = 2
        arg3 = np.array([1,2,3])
        self.assertRaises(TypeError,object_test.exp,arg1,arg2)
        self.assertRaises(TypeError,object_test.exp,arg3,arg1)

    def test_int_argument(self):
        arg1 = 10
        arg2 = 2
        self.assertRaises(TypeError,object_test.exp,arg1,arg2)
    
    def test_float_argument(self):
        arg1 = 10.10
        arg2 = 2
        self.assertRaises(TypeError,object_test.exp,arg1,arg2)

    def test_two_arrays(self):
        arg1 = np.array([1,2,3])
        arg2 = np.array([4,5,6])
        self.assertRaises(TypeError,object_test.exp,arg1,arg2)

    def test_array(self):
        arg1 = np.array([1,2,3,4])
        arg2 = 10
        array_test1 = object_test.exp(arg1,arg2)
        array_test2 = np.array([0.011109, 0.01831564, 0.03019738, 0.04978707])
        self.assertAlmostEqual(array_test1.all(),array_test2.all())

if __name__ == '__main__':
    unittest.main()