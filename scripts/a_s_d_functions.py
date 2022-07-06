import numpy as np
import math

class Functions():
    def __init__(self):
        pass
    def linear(self, t, t0):    
        """
        Linear function used to calculate the attack of the note.

        Parameters
        ----------
        t : np.array
            Time
        t0 : float
            Attack duration time
        
        Returns
        -------
        np.array
            Time array with the linear function
        """
        if type(t) != type(np.array(0)):
            raise TypeError('t must be a numpy array')

        if str(type(t0)) not in ["<class 'int'>", "<class 'float'>"]:
            raise TypeError('t0 must be of int or float type')

        if len(t) == 0:
            raise ValueError('the length of the numpy array must not be 0')

        if t0 == 0:
            t0 = 1

        return t/t0

    def exp(self, t, t0):
        """
        Exponential function used to calculate the attack of the note.

        Parameters
        ----------
        t : np.array
            Time array
        t0 : float
            Attack duration time

        Returns
        -------
        np.array
            Time array with the exponential function
        """
        if type(t) != type(np.array(0)):
            raise TypeError('t must be a numpy array')

        if str(type(t0)) not in ["<class 'int'>", "<class 'float'>"]:
            raise TypeError('t0 must be of int or float type')

        if t0 == 0:
            raise ValueError('t0 must not be 0')
        
        if len(t) == 0:
            raise ValueError('the length of the numpy array must not be 0')
        
        exp = np.exp((5*(t-t0))/t0) 
        return exp

    def quartsin(self, t, t0):
        """
        Quartic sinusoidal function used to calculate the attack of the note.

        Parameters
        ----------
        t : np.array
            Time array
        t0 : float
            Attack duration time

        Returns
        -------
        np.array
            Time array with the quartic sinusoidal function
        """
        if type(t) != type(np.array(0)):
            raise TypeError('t must be a numpy array')

        if str(type(t0)) not in ["<class 'int'>", "<class 'float'>"]:
            raise TypeError('t0 must be of int or float type')
        
        if len(t) == 0:
            raise ValueError('t must be of length different than 0')

        if t0 == 0:
            raise ValueError('t0 must not be 0')

        quartsin =  np.sin((math.pi*t)/(2*t0)) 
        return quartsin

    def halfsin(self, t, t0):
        """
        Half sinusoidal function used to calculate the attack of the note.

        Parameters
        ----------
        t : np.array
            Time array
        t0 : float
            Attack duration time

        Returns
        -------
        np.array
            Time array with the half sinusoidal function
        """
        if type(t) != type(np.array(0)):
            raise TypeError('t must be a numpy array')

        if str(type(t0)) not in ["<class 'int'>", "<class 'float'>"]:
            raise TypeError('t0 must be of int or float type')

        if t0 == 0:
            raise ValueError('t0 must not be 0')

        if len(t) == 0:
            raise ValueError('the length of the numpy array must not be 0')

        aux_calc = (t/t0) - 0.5
        halfsin= (1+np.cos((math.pi*(aux_calc))))/2 

        return halfsin

    def log(self, t, t0):
        """
        Logarithmic function used to calculate the attack of the note.

        Parameters
        ----------
        t : np.array
            Time array
        t0 : float
            Attack duration time

        Returns
        -------
        np.array
            Time array with the logarithmic function
        """
        if type(t) != type(np.array(0)):
            raise TypeError('t must be a numpy array')

        if str(type(t0)) not in ["<class 'int'>", "<class 'float'>"]:
            raise TypeError('t0 must be of int or float type')

        if len(t) == 0:
            raise ValueError('the length of the numpy array must not be 0')

        if t0 == 0:
            raise ValueError('t0 must not be 0')

        log = np.log10(((9*t)/t0)+1)

        return log

    def tri(self, t, t0, t1, a1, frate=44100):
        """
        Triangular function used to calculate the attack of the note.

        Parameters
        ----------
        t : np.array
            Time array
        t0 : float
            Attack duration time
        t1 : float
            Parameter
        a1 : float
            Parameter

        Returns
        -------
        np.array
            Time array with the triangular function
        """
        if type(t) != type(np.array(0)):
            raise TypeError('t must be a numpy array')

        if str(type(t1)) not in ["<class 'int'>",
        "<class 'float'>"]or str(type(a1)) not in ["<class 'int'>",
        "<class 'float'>"] or str(type(t0)) not in ["<class 'int'>", "<class 'float'>"]:
            raise TypeError('t0, t1 and a1 must be of int or float type')

        if t1 == 0:
            raise ValueError('t1 must not be 0')

        if t1 == t0:
            raise ValueError('t0 must not be equal to t1')

        til = int(t1*frate)

        t[:til] = (t[:til]*a1)/t1
        t[til:] = ((t[til:]-t1)/(t1-t0)) + a1

        return t

    def constant(self, duration):
        """
        Constant function used to calculate the sustain of the note.

        Parameters
        ----------
        duration : float
            Duration of the note

        Returns
        -------
        np.array
            Time array with the constant function
        """
        if type(duration) != type(np.array(0)):
            raise TypeError('t must be a numpy array')
        if len(duration) == 0:
            raise ValueError('The length of the numpy array must not be 0')

        return np.ones(len(duration))

    def invlinear(self, t, t0):
        """
        Inverse linear function used to calculate the sustain and decay of the note.

        Parameters
        ----------
        t : np.array
            Time array
        t0 : float
            Decay / sustain duration time

        Returns
        -------
        np.array
            Time array with the inverse linear function
        """
        if type(t) != type(np.array(0)):
            raise TypeError('t must be a numpy array')

        if str(type(t0)) not in ["<class 'int'>", "<class 'float'>"]:
            raise TypeError('t0 must be of int or float type')

        if len(t) == 0:
            raise ValueError('the length of the numpy array must not be 0')

        if t0 == 0:
            t0 = 1

        invl = 1 - (t/t0)
        invl[(t/t0)>1] = 0

        return t

    def sin(self, t, a, f):
        """
        Sinusoidal function used to calculate the sustain of the note.

        Parameters
        ----------
        t : np.array
            Time array
        a : float
            Amplitude
        f : float
            Frequency

        Returns
        -------
        np.array
            Time array with the sinusoidal function

        """

        if type(t) != type(np.array(0)):
            raise TypeError('t must be a numpy array')

        if str(type(a)) not in ["<class 'int'>",
        "<class 'float'>"] or str(type(f)) not in ["<class 'int'>", "<class 'float'>"]:
            raise TypeError('a and f must be of int or float type')

        if len(t) == 0:
            raise ValueError('the length of the numpy array must not be 0')

        func_sin = 1 + a*np.sin(f*t) 

        return func_sin

    def invexp(self,t,t0):
        """
        Inverse exponential function used to calculate the sustain
        and decay of the note.

        Parameters
        ----------
        t : np.array
            Time array
        t0 : float
            Decay / sustain duration time

        Returns
        -------
        np.array
            Time array with the inverse exponential function
        """
        if type(t) != type(np.array(0)): 
            raise TypeError('t must be a numpy array')

        if len(t) == 0:
            raise ValueError('the length of the numpy array must not be 0')

        if str(type(t0)) not in ["<class 'int'>", "<class 'float'>"]:
            raise TypeError('t0 must be of int or float type')

        if len(t) == 0:
            raise ValueError('the length of the numpy array must not be 0')

        if t0 == 0:
            raise ValueError('t0 must not be 0')

        invexp = np.exp((-5*t)/t0) 

        return invexp

    def quartcos(self, t, t0):
        """
        Quartic cosinusoidal function used to calculate the sustain
        and decay of the note.

        Parameters
        ----------
        t : np.array
            Time array
        t0 : float
            Decay / sustain duration time

        Returns
        -------
        np.array
            Time array with the quartic cosinusoidal function
        """
        if type(t) != type(np.array(0)):
            raise TypeError('t must be a numpy array')

        if str(type(t0)) not in ["<class 'int'>", "<class 'float'>"]:
            raise TypeError('t0 must be of int or float type')

        if t0 == 0:
            raise ValueError('t0 must not be 0')

        if len(t) == 0:
            raise ValueError('the length of the numpy array must not be 0')

        arr = (math.pi*t)/(2*t0)
        quartcos = np.cos((arr))

        return quartcos

    def invlog(self, t, t0):
        """
        Inverse logarithmic function used to calculate the sustain
        and decay of the note.

        Parameters
        ----------
        t : np.array
            Time array
        t0 : float
            Decay / sustain duration time

        Returns
        -------
        np.array
            Time array with the inverse logarithmic function
        """
        if type(t) != type(np.array(0)):
            raise TypeError('t must be a numpy array')

        if str(type(t0)) not in ["<class 'int'>", "<class 'float'>"]:
            raise TypeError('t0 must be of int or float type')
        
        if len(t) == 0:
            raise ValueError('the length of the numpy array must not be 0')

        if t0 == 0:
            raise ValueError('t0 must not be 0')

        invlog = np.log10((-9*t/t0)+10)
        invlog[t>=t0] = 0

        return invlog

    def pulses(self, t, t0, t1, a1):
        """
        Pulses function used to calculate the sustain of the note.

        Parameters
        ----------
        t : np.array
            Time array
        t0 : float
            Sustain duration time
        t1 : float
            Parameter
        a1 : float
            Parameter

        Returns
        -------
        np.array
            Time array with the pulses function
        """
        if type(t) != type(np.array(0)): 
            raise TypeError('t must be a numpy array')

        if str(type(t0)) not in ["<class 'int'>",
        "<class 'float'>"] or str(type(t1)) not in ["<class 'int'>",
        "<class 'float'>"] or str(type(a1)) not in ["<class 'int'>", "<class 'float'>"]:
            raise TypeError('t0, t1 and a1 must be of int or float type')

        if len(t) == 0:
            raise ValueError('the length of the numpy array must not be 0')

        if t0 == 0 or t1 == 0: 
            raise ValueError('t0 and t1 must not be 0')

        t_ = (t/t0) - np.absolute(t/t0) 
        pulses_two =  np.floor(abs(((1-a1)/t1)*(t_ - t0 + t1)) + 1)

        return pulses_two

    def halfcos(self, t, t0):
        """
        Halfcos function is used to calculate the sustain and decay of the note.

        Parameters
        ----------
        t : np.array
            Time array
        t0 : float
            Decay / sustain duration time
        
        Returns
        -------
        np.array
            Time array with the halfcos function
        """
        if type(t) != type(np.array(0)): 
            raise TypeError('t must be a numpy array')

        if str(type(t0)) not in ["<class 'int'>", "<class 'float'>"]:
            raise TypeError('t0 must be of int or float type')
        
        if len(t) == 0:
            raise ValueError('the length of the numpy array must not be 0')

        if t0 == 0:
            t0 == 1

        invhalfcos = 1 - ((np.cos(math.pi*t/ 2*t0)) / 2) 

        return invhalfcos