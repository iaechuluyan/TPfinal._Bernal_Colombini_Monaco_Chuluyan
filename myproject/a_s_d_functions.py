
import numpy as np
import math



class Functions():
    def __init__(self):
        pass
    def func_linear(self, t, t0): #A
        """
        Linear function used to calculate the attack time.

        Parameters
        ----------
        t : float
            time
        t0 : float
            time duration

        Returns
        -------
        float
            value of function
        """
        if type(t) != type(np.array(0)):  #asi se dice el type?
            raise TypeError('t must be a numpy array')

        if type(t0) not in [int, float]:
            raise TypeError('t0 must be of int or float type')

        if t0 == 0:
            raise ValueError('t0 must not be 0')

        return t/t0

    def exp(self, t, t0): #A
        """
        Exponential function used to calculate the attack time.

        Parameters
        ----------
        t : float
            time
        t0 : float
            time duration

        Returns
        -------
        float
            value of function
        """
        if type(t) != type(np.array(0)):  #asi se dice el type?
            raise TypeError('t must be a numpy array')

        if type(t0) not in [int, float]:
            raise TypeError('t0 must be of int or float type')

        if t0 == 0:
            raise ValueError('t0 must not be 0')
        
        exp = np.exp((5*(t-t0))/t0) 
        return exp

    def quartsin(self, t, t0): #A
        """
        Quartic sinusoidal function used to calculate the attack time.

        Parameters
        ----------
        t : float
            time
        t0 : float
            time duration

        Returns
        -------
        float
            value of function
        """
        if type(t) != type(np.array(0)):  #asi se dice el type?
            raise TypeError('t must be a numpy array')

        if type(t0) not in [int, float]:
            raise TypeError('t0 must be of int or float type')

        if t0 == 0:
            raise ValueError('t0 must not be 0')

        quartsin =  np.sin((math.pi*t)/(2*t0)) 
        return quartsin

    def halfsin(self, t, t0): #A
        """
        Half sinusoidal function used to calculate the attack time.

        Parameters
        ----------
        t : float
            time
        t0 : float
            time duration

        Returns
        -------
        float
            value of function
        """
        if type(t) != type(np.array(0)):  #asi se dice el type?
            raise TypeError('t must be a numpy array')

        if type(t0) not in [int, float]:
            raise TypeError('t0 must be of int or float type')

        if t0 == 0:
            raise ValueError('t0 must not be 0')

        aux_calc = (t/t0) - 0.5
        halfsin= (1+np.cos((math.pi*(aux_calc))))/2 

        return halfsin

    def log(self, t, t0): #A
        """
        Logarithmic function used to calculate the attack time.

        Parameters
        ----------
        t : float
            time
        t0 : float
            time duration

        Returns
        -------
        float
            value of function
        """
        if type(t) != type(np.array(0)):  #asi se dice el type?
            raise TypeError('t must be a numpy array')

        if type(t0) not in [int, float]:
            raise TypeError('t0 must be of int or float type')

        if t0 == 0:
            raise ValueError('t0 must not be 0')

        log = np.log10(((9*t)/t0)+1)

        return log

    def tri(self, t, t0, t1, a1): #ACA A
        """
        Triangular function used to calculate the attack time.

        Parameters
        ----------
        t : float
            time
        t0 : float
            time duration
        t1 : float
       
        a1 : float

        Returns
        -------
        float
            value of function
        """
        if type(t) != type(np.array(0)):  #asi se dice el type?
            raise TypeError('t must be a numpy array')

        if type(t1) not in [int, float] or type(a1) not in [int, float] or type(t0) not in [int, float]:
            raise TypeError('t0, t1 and a1 must be of int or float type')

        if t1 == 0:
            raise ValueError('t1 must not be 0')

        if t1 == t0:
            raise ValueError('t0 must not be equal to t1')

        tri = np.zeros(len(t))
        for idx in range (0, len(t)):
            if t[idx] < t1:
                tri[idx] = (t*a1)/t1
            elif t[idx] > t1:
                tri[idx] = ((t-t1)/(t1-t0)) + a1

        # t[t<t1] = (t*a1)/t1
        # t[t>t1] = ((t-t1)/(t1-t0)) + a1 #valueerror  NumPy boolean array indexing assignment cannot assign 2685 input values to the 0 output values where the mask is true

        return tri #t

    def func_constant(self, duration): #S
        """
        Constant function used to calculate the sustain time.

        Returns
        -------
        int
            value of function
        """
        if type(duration) != type(np.array(0)):  #asi se dice el type?
            raise TypeError('t must be a numpy array')

        return np.ones(len(duration))

    def func_invlinear(self, t, t0): #S, D
        """
        Inverse linear function used to calculate the sustain time.

        Parameters
        ----------
        t : float
            time
        t0 : float
            time duration

        Returns
        -------
        float
            value of function
        """
        if type(t) != type(np.array(0)):  #asi se dice el type?
            raise TypeError('t must be a numpy array')

        if type(t0) not in [int, float]:
            raise TypeError('t0 must be of int or float type')

        if t0 == 0:
            raise ValueError('t0 must not be 0')

        invl = np.zeros(len(t))
        for idx in range (0, len(t)):
            if (t[idx]/t0) < 1:
                invl[idx] = 1- (t[idx]/t0)
            else:
                invl[idx] = 0


        # t[(t/t0)<1] = 1 - (t/t0)
        # t[(t/t0)>1] = 0
        
        return t

    def func_sin(self, t, a, f): #S
        """
        Sinusoidal function used to calculate the sustain time.

        Parameters
        ----------
        t : float
            time
        a : float
            amplitude
        f : float
            frequency

        Returns
        -------
        float
            value of function
        """
        if type(t) != type(np.array(0)):  #asi se dice el type?
            raise TypeError('t must be a numpy array')

        if type(a) not in [int, float] or type(f) not in [int, float]:
            raise TypeError('a and f must be of int or float type')


        func_sin = 1 + a*np.sin(f*t) 

        return func_sin

    def invexp(self,t,t0): #S, D
        """
        Inverse exponential function used to calculate the sustain time.

        Parameters
        ----------
        t : float
            time
        t0 : float
            time duration

        Returns
        -------
        float
            value of function
        """
        if type(t) != type(np.array(0)):  #asi se dice el type?
            raise TypeError('t must be a numpy array')

        if type(t0) not in [int, float]:
            raise TypeError('t0 must be of int or float type')

        if t0 == 0:
            raise ValueError('t0 must not be 0')

        invexp = np.exp((-5*t)/t0) 

        return invexp

    def quartcos(self, t, t0): #S, D
        """
        Quartic cosinusoidal function used to calculate the sustain time.

        Parameters
        ----------
        t : float
            time
        t0 : float
            time duration

        Returns
        -------
        float
            value of function
        """
        if type(t) != type(np.array(0)):  #asi se dice el type?
            raise TypeError('t must be a numpy array')

        if type(t0) not in [int, float]:
            raise TypeError('t0 must be of int or float type')

        if t0 == 0:
            raise ValueError('t0 must not be 0')

        arr = (math.pi*t)/(2*t0)
        quartcos = np.cos((arr))


        return quartcos

    def invlog(self, t, t0): #S, D
        """
        Inverse logarithmic function used to calculate the sustain time.

        Parameters
        ----------
        t : float
            time
        t0 : float
            time duration

        Returns
        -------
        float
            value of function
        """
        if type(t) != type(np.array(0)):  #asi se dice el type?
            raise TypeError('t must be a numpy array')

        if type(t0) not in [int, float]:
            raise TypeError('t0 must be of int or float type')

        if t0 == 0:
            raise ValueError('t0 must not be 0')

        invlog= np.zeros(len(t))
        for idx in range (0, len(t)):
            if t[idx] < t0:
                invlog[idx] = np.log10((-9*t/t0)+10)
            elif t[idx] > t0:
                invlog[idx] = 0

        # t[t<t0] = np.log10((-9*t/t0)+10) #error
        # t[t>t0] = 0

        return t

    def pulses(self, t, t0, t1, a1): #S
        """
        Pulses function used to calculate the sustain time.

        Parameters
        ----------
        t : float
            time

        t0 : float
            time duration
        t1 : float
           
        a1 : float
   
        Returns
        -------
        float
            value of function
        """
        if type(t) != type(np.array(0)):  #asi se dice el type?
            raise TypeError('t must be a numpy array')

        if type(t0) not in [int, float] or type(t1) not in [int, float] or type(a1) not in [int, float]:
            raise TypeError('t0, t1 and a1 must be of int or float type')

        if t0 == 0 or t1 == 0: 
            raise ValueError('t0 and t1 must not be 0')

        print(t/t0)
        t_ = (t/t0) - np.absolute(t/t0) 
        pulses_two =  np.floor(abs(((1-a1)/t1)*(t_ - t0 + t1)) + 1)

        return pulses_two

    def halfcos(self, t, t0): #S, D
        """
        Halfcos function is used to calculate the decay time.

        Parameters
        ----------
        t : float
            Time.
        t0 : float
            Time duration.

        Returns
        -------
        float
            value of function

        """
        if type(t) != type(np.array(0)):  #asi se dice el type?
            raise TypeError('t must be a numpy array')

        if type(t0) not in [int, float]:
            raise TypeError('t0 must be of int or float type')

        if t0 == 0:
            raise ValueError('t0 must not be 0')

        invhalfcos = 1 - ((np.cos(math.pi*t/ 2*t0)) / 2) 

        return invhalfcos
   