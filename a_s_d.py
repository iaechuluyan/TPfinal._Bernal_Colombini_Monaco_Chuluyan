import math
class Atack():
    def __init__(self):
        pass
    def func_linear(self,t: float, t0: float) -> float:
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
        return math.exp((5*(t-t0))/t0)

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
        return math.sin((math.pi*t)/(2*t0))

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
        return (1+math.cos((math.pi*t)/t0))/2

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
        return math.log(((9*t)/10)+1,10)

    def tri(self, t: float, t0: float, t1: float, a1: float) -> float:
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
        if t < t1:
            return (t*a1)/t1
        elif t > t1:
            return ((t-t1)/(t1-t0)) + a1

class Sustain():
    def __init__(self):
        pass
    def func_constant(self) -> int:
        """
        Constant function used to calculate the sustain time.

        Returns
        -------
        int
            value of function
        """
        return 1

    def func_invlinear(self,t,t0) -> float:
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
        if t/t0 < 1:
            return 1 - (t/t0)
        elif t/t0 >= 1:
            return 0

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
        return 1+ a*math.sin(f*t)

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
        return math.exp((-5*t)/t0)

    def quartcos(self, t: float, t0: float) -> float:
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
        return math.cos((math.pi*t)/(2*t0))

    def halfcos(self, t: float, t0: float) -> float:
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
        return (1+math.cos((math.pi*t)/t0))/2

    def invlog(self, t: float, t0: float) -> float:
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
        if t < t0:
            return math.log((-9*t/t0) +10,10)
        else:
            return 0

    def pulses(self, t: float, t0: float, t1: float, a1: float) -> float:
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
        import math
        t_ = (t/t0) - math.floor(t/t0)
        return min(abs(((1-a1)/t1)(t_ - t0 + t1)) + a1)

class decay:
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
        return 1 - (math.exp(-t / t0))

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
        return 1 - (math.cos(t / t0)) ** 4

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
        return 1 - (math.cos(t / t0)) ** 2
    

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
        return 1 - (math.log(t / t0))
