import unittest
from read_txt_files import music_sheet, get_frequency

class TestNotesFrequency(unittest.TestCase):

    def test_music_sheet (self):
        """ Test the music_sheet function """
        self.assertEqual([[0.0, 440.0, 0.5], [0.5, 466.164, 0.5],
        [1.0, 493.883, 0.5],[1.5, 261.626, 0.5], [2.0, 261.626, 0.5],
        [2.5, 293.665, 0.5]],music_sheet("scale.txt"))
        
    def test_get_frequency (self):
        """ Test the get_frequency function """
        self.assertEqual(466.164, get_frequency("Bb4"))
        self.assertEqual(493.883, get_frequency("B4"))
        self.assertEqual(440.0, get_frequency("C4")) # This line should fail
        