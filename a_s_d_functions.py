
import numpy as np
import math

def funct(hola):
    print(f"hola {hola}")
dic = {"not": funct}

class Attack():
    def __init__(self):
        pass
    def func_linear(self, t: float, t0: float) -> float:
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

    def exp(self, t: float, t0: float) -> float:
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
        exp = np.zeros(len(t))
        for idx in range(0, len(t)):
            exp[idx]= math.exp((5*(t[idx]-t0))/t0)

        return exp

    def quartsin(self, t: float, t0: float) -> float:
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
        quartsin = np.zeros(len(t))
        for idx in range(0, len(t)):
            quartsin[idx]= math.sin((math.pi*t[idx])/(2*t0))

        return quartsin

    def halfsin(self, t: float, t0: float) -> float:
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
        halfsin = np.zeros(len(t))
        for idx in range(0, len(t)):
            aux_calc = (t[idx]/t0)-(1/2)
            halfsin[idx] = (1+math.cos((math.pi*(aux_calc))))/2

        return halfsin

    def log(self, t: float, t0: float) -> float:
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
        log = np.zeros(len(t))
        for idx in range(0, len(t)):
            log[idx] = math.log(((9*t[idx])/t0)+1,10)

        return log

    def tri(self, t: float, t0: float, t1: float, a1: float) -> float: #ACA
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
        T = np.zeros(len(t))
        for idx in range(0, len(t)):
            if t[idx] < t1:
                T[idx] = (t[idx]*a1)/t1
            elif t[idx] > t1:
                T[idx] = ((t[idx]-t1)/(t1-t0)) + a1
        
        return T


class Sustain():
    def __init__(self):
        pass
    def func_constant(self, duration) -> int:
        """
        Constant function used to calculate the sustain time.

        Returns
        -------
        int
            value of function
        """
        return np.ones(len(duration))

    def func_invlinear(self, t,t0, decay_start) -> float:
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
        invlinear = 1 - (t - decay_start)/t0#restarle cdo empieza el decay
        for idx in range(0, len(invlinear)):
            if invlinear[idx] > 0:
                continue
            else:
                invlinear[idx] = 0
        
        return invlinear

    def func_sin(self, t: float, a: float, f: float) -> float:
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
        func_sin = np.zeros(len(t))
        for idx in range(0, len(t)):
            func_sin[idx]= 1 + a*math.sin(f*t[idx])

        return func_sin

    def invexp(self,t: float,t0: float) -> float:
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
        invexp = np.zeros(len(t))
        for idx in range(0, len(t)):
            invexp[idx] = math.exp((-5*t[idx])/t0)

        return invexp

    def quartcos(self, t: float, t0: float) -> float: #
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
        quartcos = np.zeros(len(t))
        for idx in range(0, len(t)):
            quartcos[idx] = math.cos((math.pi*t[idx])/(2*t0))


        return quartcos

    def halfcos(self, t: float, t0: float) -> float: #
        """
        Half cosinusoidal function used to calculate the sustain time.

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
        halfcos = np.zeros(len(t))
        for idx in range(0, len(t)):
            halfcos[idx] = (1+math.cos((math.pi*t[idx])/t0))/2

        return halfcos


    def invlog(self, t: float, t0: float) -> float: #!!!
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
        invl = np.zeros(len(t))
        for idx in range(0, len(t)):
            if invl[idx] < t0:
                invl[idx] = math.log((-9*t[idx]/t0)+10, 10)
            else:
                invl[idx] = 0

        return invl

    def pulses(self, t: float, t0: float, t1: float, a1: float) -> float: #!!! 
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
        t_ = np.zeros(len(t))
        T_ = np.zeros(len(t))
        for idx in range (0, len(t)):
            t_[idx] = (t[idx]/t0) - math.floor(t[idx]/t0)
            T_[idx] = abs(int((((1-a1)/t1)(t_[idx] - t0 + t1)) + a1))

        return min(T_)

class Decay: ##### no nec modificarse xq aca si que allows la division, es uno menos tatata igual?
    def _init_(self):
        pass

    def invlinear(self, t: float, t0: float) -> float:
        """
        Invlinear function is used to calculate the decay time.

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
        return 1 - (t / t0)

    def invexp(self, t: float, t0: float) ->float:
        """
        Invexp function is used to calculate the decay time.

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
        invexp = np.zeros(len(t))
        for idx in range (0, len(t)):
            invexp[idx] = 1 - (math.exp(-t[idx] / t0))

        return invexp

    def quartcos(self, t: float, t0: float) ->float:
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
        invquartcos = np.zeros(len(t))
        for idx in range (0, len(t)):
            invquartcos[idx] = 1 - (math.cos(t[idx] / t0)) ** 4

        return invquartcos

    def halfcos(self, t: float, t0: float) ->float:
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
        invhalfcos = np.zeros(len(t))
        for idx in range (0, len(t)):
            invhalfcos[idx] = 1 - (math.cos(t[idx]/ t0)) ** 2

        return invhalfcos
   

    def invlog(self, t: float, t0: float) ->float:
        """
        Invlog function is used to calculate the decay time.

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
        invlog = np.zeros(len(t))
        for idx in range (0, len(t)):
            invlog[idx] = 1 - (math.log(t[idx] / t0))

        return invlog


#chequear graficos
#chequear tema tiempos, como pasarlo pa que quede mejor, sobretodo cdo el tiempo pasa (en secs), y se hace mas grande