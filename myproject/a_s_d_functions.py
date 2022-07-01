
import numpy as np
import math

# def funct(hola):
#     print(f"hola {hola}")
# dic = {"not": funct}

class Functions():
    def __init__(self):
        pass
    def func_linear(self, t, t0):
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
        return t/t0

    def exp(self, t, t0):
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

        exp = math.exp((5*(t-t0))/t0)
        return exp

    def quartsin(self, t, t0):
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
        quartsin =  math.sin((math.pi*t)/(2*t0))
        return quartsin

    def halfsin(self, t, t0):
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
        aux_calc = (t/t0) - 0.5
        halfsin= (1+math.cos((math.pi*(aux_calc))))/2

        return halfsin

    def log(self, t, t0):
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
        log = math.log(((9*t)/t0)+1,10)

        return log

    def tri(self, t, t0, t1, a1): #ACA
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
        t[t<t1] = (t*a1)/t1
        t[t>t1] = ((t-t1)/(t1-t0)) + a1

        return t

    def func_constant(self, duration):
        """
        Constant function used to calculate the sustain time.

        Returns
        -------
        int
            value of function
        """
        return np.ones(len(duration))

    def func_invlinear(self, t,t0): #A
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

        invl = np.zeros(len(t))
        for idx in range (0, len(t)):
            if (t[idx]/t0) < 1:
                invl[idx] = 1- (t[idx]/t0)
            else:
                invl[idx] = 0


        # t[(t/t0)<1] = 1 - (t/t0)
        # t[(t/t0)>1] = 0
        
        return invl

    def func_sin(self, t, a, f):
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
        func_sin = 1 + a*math.sin(f*t)

        return func_sin

    def invexp(self,t,t0):
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
        invexp = math.exp((-5*t)/t0)

        return invexp

    def quartcos(self, t, t0): 
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
        quartcos = math.cos((math.pi*t)/(2*t0))


        return quartcos

    def invlog(self, t, t0): #A
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
        t[t<t0] = math.log((-9*t/t0)+10, 10)
        t[t>t0] = 0

        return t

    def pulses(self, t, t0, t1, a1): #A
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
        print(t/t0)
        t_ = (t/t0) - abs(t/t0)
        pulses_two =  math.floor(abs(((1-a1)/t1)*(t_ - t0 + t1)) + 1)

        return pulses_two

    def quartcos(self, t, t0): 
        """
        Quartcos function is used to calculate the decay time.

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
        invquartcos = 1 - (math.cos(math.pi*t/ 2*t0))

        return invquartcos

    def halfcos(self, t, t0):
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
        invhalfcos = 1 - ((math.cos(math.pi*t/ 2*t0)) / 2)

        return invhalfcos