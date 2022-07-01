import unittest, math
from a_s_d import Attack, Sustain, Decay

class TestAttackFunctions(unittest.TestCase):
    def test_func_linear (self):
        """ Test the linear function 
        """
        self.assertEqual(0.5, Attack.func_linear(0.25, 0.5))
        self.assertEqual(1, Attack.func_linear(0.5, 0.5))
        self.assertEqual(0.5, Attack.func_linear(0.5, 0.5)) # This line should fail

    def test_func_exp (self):
        """ Test the exponential function 
        """
        self.assertTrue(0.081<Attack.exp(0.25, 0.5)<0.083)
        self.assertEqual(1, Attack.exp(0.5, 0.5))
        self.assertEqual(0, Attack.exp(0.75, 0.5)) # This line should fail

    def test_func_quartsin (self):
        """ Test the quartsin function
        """
        self.assertEqual(0, Attack.quartsin(1, 2))
        self.assertEqual(-1, Attack.quartsin(2, 1))
        self.assertEqual(0, Attack.quartsin(3, 2)) # This line should fail
    
    def test_func_halfsin (self):
        """ Test the halfsin function
        """
        self.assertEqual(1, Attack.halfsin(1, 2))
        self.assertEqual(0, Attack.halfsin(3, 2))
        self.assertEqual(0, Attack.halfsin(2, 2)) # This line should fail

class TestSustainFunctions(unittest.TestCase):

    def test_func_constant (self):
        """ Test the constant function
        """
        self.assertEqual(1, Sustain.func_constant())
        self.assertEqual(-1, Sustain.func_constant()) # This line should fail

    def test_func_invlinear (self):
        """ Test the invlinear function
        """
        self.assertEqual(0.5, Sustain.func_invlinear(0.25, 0.5))
        self.assertEqual(1, Sustain.func_invlinear(0, 0.5))
        self.assertEqual(0.5, Sustain.func_invlinear(3, 2)) # This line should fail

    def test_func_sin(self):
        """ Test the sin function
        """
        self.assertEqual(1, Sustain.func_sin(1, 0.25, math.pi))
        self.assertEqual(1.25, Sustain.func_sin(1, 0.25, math.pi/2))
        self.assertEqual(0.5, Sustain.func_sin(1, 1, math.pi/6)) # This line should fail

    def test_func_invexp(self):
        """ Test the invexp function
        """
        self.assertEqual(math.e, Sustain.func_invexp(-1, 5))
        self.assertEqual(1, Sustain.func_invexp(0, 0.5))
        self.assertEqual(math.e, Sustain.func_invexp(1, 5))

    def test_func_quartcos(self):
        """ Test the quartcos function
        """
        self.assertEqual(0, Sustain.func_quartcos(1, 1))
        self.assertEqual(-1, Sustain.func_quartcos(2, 1))
        self.assertEqual(0, Sustain.func_quartcos(0, 1)) # This line should fail

    def test_func_halfcos(self):
        """ Test the halfcos function
        """
        self.assertEqual(0, Sustain.func_halfcos(1, 1))
        self.assertEqual(0.5, Sustain.func_halfcos(1, 2))
        self.assertEqual(0, Sustain.func_halfcos(0, 1)) # This line should fail

    def test_func_invlog(self):
        """ Test the invlog function
        """
        self.assertEqual(1, Sustain.func_invlog(0, 1))
        self.assertTrue(0.95<Sustain.func_invlog(1, 9)<0.96)
        self.assertEqual(1, Sustain.func_invlog(3, 2)) # This line should fail

    def test_func_pulses(self):
        pass

class TestDecayFunctions(unittest.TestCase):
    def test_func_invlinear(self):
        """ Test the invlinear function
        """
        self.assertEqual(Decay.invlinear(0.30 , 0.60))
        self.assertEqual(Decay.invlinear(0.20 , 0.40))
        self.assertEqual(Decay.invlinear(0.4 , 0.0)) # This line should fail
    
    def test_func_invexp(self):
        """ Test the invexp function
        """
        self.assertEqual(Decay.invexp(0, 1))
        self.assertEqual(Decay.invexp(0.5, 1))
        self.assertEqual(Decay.invexp(0,5, 0)) # This line should fail 

    def test_func_quartcos(self):
        """ Test the quartcos function
        """
        self.assertEqual(Decay.quartcos(2, 2))
        self.assertEqual(Decay.quartcos(1.2, 2.1))
        self.assertEqual(Decay.quartcos(2, 0)) # This line should fail

    def test_func_halfcos(self):
        """ Test the halfcos function
        """
        self.assertEqual(Decay.halfcos(2, 4))
        self.assertEqual(Decay.halfcos(0.3, 0.6))
        self.assertEqual(Decay.halfcos(8, 0)) # This line should fail

    def test_func_invlog(self):
        """ Test the invlog function
        """
        self.assertEqual(Decay.invlog(0, 2))
        self.assertEqual(Decay.invlog(0.5, 1))
        self.assertEqual(Decay.invlog(0.8, 0)) # This line should fail