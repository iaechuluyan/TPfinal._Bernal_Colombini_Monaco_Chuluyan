import unittest
import numpy as np
from sorting import sorting_notes

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
        self.assertRaises(TypeError,sorting_notes,arg1)

    def test_list(self):
        list_test1 = [[2.0, 293.665, 5.0],[0.0, 261.626, 2.0], [3.0, 329.628, 4.0], [4.0, 349.228, 6.0]]
        sorting_notes(list_test1)
        list_test2 = [[0.0, 261.626, 2.0], [3.0, 329.628, 4.0],[2.0, 293.665, 5.0], [4.0, 349.228, 6.0]]
        self.assertEqual(list_test1,list_test2)

if __name__ == '__main__':
    unittest.main()