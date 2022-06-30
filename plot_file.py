
import wave
import matplotlib as plt
import numpy as np

def plot():
    '''
    
    '''
    spf = wave.open("final.wav", "r")
    signal = spf.readframes(-1)
    signal = np.fromstring(signal, "int16")
    plt.figure(1)
    plt.title("Signal Wave...")
    plt.plot(signal)
    plt.show()
    plt.subplot()
    