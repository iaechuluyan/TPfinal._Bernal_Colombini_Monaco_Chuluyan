import unittest
import numpy as np
from a_s_d_functions import Functions

object_test = Functions()

class TestTri(unittest.TestCase):
    def test_empty_array_argument(self):
        arg1 = np.array([1,2,3])
        arg2 = 2
        arg3 = np.array([])
        self.assertRaises(TypeError,object_test.tri,arg1,arg2,arg2,arg3)
        self.assertRaises(TypeError,object_test.tri,arg1,arg2,arg3,arg2)
        self.assertRaises(TypeError,object_test.tri,arg1,arg3,arg2,arg2)
        self.assertRaises(ValueError,object_test.tri,arg3,arg2,arg2,arg2)

    def test_none_argument(self):
        arg1 = np.array([1,2,3])
        arg2 = 2
        arg3 = None
        self.assertRaises(TypeError,object_test.tri,arg1,arg2,arg2,arg3)
        self.assertRaises(TypeError,object_test.tri,arg1,arg2,arg3,arg2)
        self.assertRaises(TypeError,object_test.tri,arg1,arg3,arg2,arg2)
        self.assertRaises(TypeError,object_test.tri,arg3,arg2,arg2,arg2)
    
    def test_string_argument(self):
        arg1 = np.array([1,2,3])
        arg2 = 2
        arg3 = "[1,2,3]"
        self.assertRaises(TypeError,object_test.tri,arg1,arg2,arg2,arg3)
        self.assertRaises(TypeError,object_test.tri,arg1,arg2,arg3,arg2)
        self.assertRaises(TypeError,object_test.tri,arg1,arg3,arg2,arg2)
        self.assertRaises(TypeError,object_test.tri,arg3,arg2,arg2,arg2)

    def test_int_argument(self):
        arg1 = 10
        arg2 = 2
        self.assertRaises(TypeError,object_test.tri,arg1,arg2,arg2,arg2)
    
    def test_float_argument(self):
        arg1 = 10.20
        arg2 = 2
        self.assertRaises(TypeError,object_test.tri,arg1,arg2,arg2,arg2)
    
    def test_array(self):
        arg1 = np.array([1,2,3])
        arg2 = 7
        arg3 = 5
        arg4 = 6
        array_test1 = object_test.tri(arg1,arg2,arg3,arg4)
        array_test2 = np.array([1.,1.,1.])
        self.assertEqual(array_test1.all(),array_test2.all())

if __name__ == '__main__':
    unittest.main()
    