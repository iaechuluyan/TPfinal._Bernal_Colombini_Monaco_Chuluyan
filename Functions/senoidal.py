import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from numpy import arange, sin, pi


def fundamental_frequency(A=1, f=440):

    x = arange(0.0000, 0.030, 0.00001 )
    y = A*sin(2*pi*x*f)
    plt.plot(x, y)
    plt.grid(axis='both')
    plt.ylabel('y')
    plt.xlabel('x')

    plt.show()
    return y


