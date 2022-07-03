import unittest
import numpy as np
from read_txt_files import sorting_notes

class TestSortingNotes(unittest.TestCase):
    def test_array_argument(self):
        arg1 = np.array([1,2,3,4])
        self.assertRaises(TypeError,sorting_notes,arg1)

    def test_none_argument(self):
        arg1 = None
        self.assertRaises(TypeError,sorting_notes,arg1)
    
    def test_string_argument(self):
        arg1 = "[1,2,3]"
        self.assertRaises(TypeError,sorting_notes,arg1)

    def test_int_argument(self):
        arg1 = 10
        self.assertRaises(TypeError,sorting_notes,arg1)
    
    def test_float_argument(self):
        arg1 = 10.10
        self.assertRaises(ValueError,sorting_notes,arg1)

    def test_list(self):
        list_test1 = [1,4,-2,0]
        sorting_notes(list_test1)
        list_test2 = [-2,0,1,4]
        self.assertEqual(list_test1,list_test2)

if __name__ == '__main__':
    unittest.main()