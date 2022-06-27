
from re import A
import wave
import numpy as np
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import contextlib
from read_txt_files import music_sheet_info, harmonics_info, modulation_info
import sys
from modularizacion import Attack, Sustain, Decay

Attack = Attack
Sustain = Sustain
Decay = Decay

def main (frate):
    length = music_sheet_info[-1][2]
    s_audio = np.zeros(length * frate)
    writing_wave (create_sine_each_note(s_audio, 44100))

def writing_wave (s_audio, frate = 44100):
    '''
    Writes the data on the wav file.

    Parameters
    ----------
        s_audio : numpy array
        frate : frame rate

    Returns 
    -------
        None

    '''
    s_audio = (s_audio * (2 ** 15 - 1)).astype('<h')
    s_audio = s_audio.tobytes()
    with wave.open('final.wav', 'w') as w:
        w.setnchannels(1)
        w.setsampwidth(2) 
        w.setframerate(frate) 
        w.setnframes(2) 
        w.writeframes(s_audio)


def create_sine_each_note (s_audio, frate = 44100):
    '''
    Iterates over the list of notes and harmonics, appends the data to a numpy array.

    Parameters
    ----------
        s_audio : empty list
        frate : frame rate

    Returns 
    -------
        s_audio : numpy array
            The array with the appended data.

    '''
    for note in music_sheet_info:
        h = []
        for frequency_change, amplitude in (harmonics_info):
            S = harmonics(note[0], note[2], float(amplitude), float(note[1] * float(frequency_change)), h, frate)
            if type(h) is not list:
                h.sum_sine(S)
            else:
                h = S

        

        starting_i = int(h.start * frate)
        until_i = int((h.duration) * frate) 
        h.modularizar(frate)
        info = h.get_data()
       
        for c, i in zip((range(starting_i, until_i)), (range(0, len(info)))):
            s_audio[c] += info[i]     

    return s_audio

class harmonics: 
    '''


    '''
    def __init__(self, start, duration, amplitude, frequency, h, frate):
        self.start = start
        self.duration = duration 
        self.frequency = frequency
        self.amplitude = amplitude

        t = np.linspace(self.start, self.duration, frate) 
        self.sine =  self.amplitude * np.sin(2* np.pi * self.frequency * t) 
        

        # superpuestas: videos de yt del italiano

    def sum_sine (self, sin):
        self.sine = sum([self.sine, sin.get_data()])

    def modularizar (self, frate):
         attack = float(modulation_info[0][1]) * frate 
         decay = float(modulation_info[2][1]) * frate
         sustain = self.duration*frate - self.start*frate - attack - decay

         at = np.linspace(0, attack/3, frate)
         ta= attack/3
         A = Attack.func_linear(self, at, ta) #

         dt = np.linspace(sustain/3, decay/3, frate)
         td= decay/3
         D = Decay.func_invlinear(dt, td)

         st = np.linspace(attack/3, sustain/3, frate)
         S = Sustain.func_constant()

         self.sine[:attack] * A
         self.sine[attack:sustain] * S
         self.sine[sustain:] * D

        #  while t < attack:
        #      self.sine[t] = self.sine[t] / 2
        #      t+=1

        #      #de tal a tal (slicing) multiplicame creciendo
        #      #tiene que tomar como argumento el valor y retornar uno nuevo, tipo reemplazalo

        #  while t < sustain:
        #      t+=1

        #  while t < decay:
        #      self.sine[t] = self.sine[t] * 2
        #      t+=1



    def get_data (self):
        return self.sine

    def __repr__(self):
        return self.i

    def __str__(self):
        return str(self.i)


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
    



main(frate=44100)
plot()




#