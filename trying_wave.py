import wave
import numpy as np
import matplotlib.pyplot as plt
import 



def writing_wave_file ():
    t = np.linspace(0, 1, 44100)
    audio = (0.5 * sin * (2 ** 15 - 1)).astype("<h")

    with wave.open("wavfile.wav", "w") as f:
        # f.setnchannels(1)
        # f.setsampwidth(2)
        # f.setframerate(44100)
        f.setparams((1, 2, 44100, 1, None, 'NONE')) #el uno del medio corresponde a number of frames, es momentaneo
        f.writeframes(audio.tobytes())


def plot_wave ():
    spf = wave.open("wavfile.wav", "r")

    signal = spf.readframes(-1)
    signal = np.fromstring(signal, "Int16")


    plt.figure(1)
    plt.title("Signal Wave...")
    plt.plot(signal)
    plt.show()

writing_wave_file()
plot_wave()