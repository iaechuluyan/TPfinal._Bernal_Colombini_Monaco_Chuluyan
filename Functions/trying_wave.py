import wave
import numpy as np
import matplotlib.pyplot as plt
from senoidal import fundamental_frequency 


def writing_wave_file ():
    t = np.linspace(0, 1, 44100)
    audio = 0.5 * np.sin(2 * np.pi * 440.0 * t)

    with wave.open("wavfile.wav", "w") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(44100)
        #f.setcomptype(None, 'NONE')
        f.setnframes(1)
        f.writeframes(audio.tobytes())



def plot_wave ():
    spf = wave.open("wavfile.wav", "r")

    signal = spf.readframes(-1)
    signal = np.frombuffer(signal)


    plt.figure(1)
    plt.title("Signal Wave...")
    plt.plot(signal)
    plt.show()

writing_wave_file()
plot_wave()