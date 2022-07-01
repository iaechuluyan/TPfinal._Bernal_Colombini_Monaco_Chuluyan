import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from numpy import arange, sin, pi


def fundamental_frequency(A=1, f=440):
    """ Calculate the fundamental frequency of a sine wave. 

    A: Amplitude of the sine wave. Default is 1.
    f: Frequency of the sine wave. Default is 440.
    
    Returns: The fundamental frequency of the sine wave.
    
    """

    x = arange(0.0000, 0.030, 0.00001 )
    y = A*sin(2*pi*x*f)
    # plt.plot(x, y)
    # plt.grid(axis='both')
    # plt.ylabel('y')
    # plt.xlabel('x')

    # plt.show()
    return y


