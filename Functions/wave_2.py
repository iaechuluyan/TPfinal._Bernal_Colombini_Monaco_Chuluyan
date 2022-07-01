from re import I
import wave
import numpy as np
import math
import matplotlib.pyplot as plt
import contextlib
from read_txt_files import music_sheet_info, harmonics_info

frate = 44100
s_audio = []

#una lista cn los a de cada nota (multiplica y q es la suma de los armonicos con m que es el que pone ASD)
#esa lista es la que después agarramos para meter en el wav

class sintetizador:
    def __init__(self, start, duration, amplitude, frequency, i, a):
        global s_audio
        self.start = start
        self.duration = duration + start
        self.frequency = frequency
        self.amplitude = amplitude
        self.i = i

        t = np.arange(self.start, self.duration, 1 / frate) #que el de duration sea cdo termina
        sine =  self.amplitude * np.sin(2* np.pi * self.frequency * t)
        self.sine = (sine * (2 ** 15 - 1)).astype("<h") 
        if len(a) != 0:
            a = np.concatenate((a, self.sine))
        else:
            a = self.sine
        
       
        # superpuestas: videos de yt del italiano

    def get_data (self):
        return self.sine

    def __repr__(self):
        return self.i

    def __str__(self):
        return str(self.i)

def create_sine_each_note ():
    """ Create a sine wave for each note in the music sheet and return a list of sine waves. 
    """
    global s_audio
    i = 0
    for note in music_sheet_info:
        a = []
        for amplitude,frequency_change in (harmonics_info):
            S = sintetizador (note[0], note[2], int(amplitude), int(frequency_change) * note[1], i, a)
            i+=1
        s_audio = np.concatenate(s_audio, a)


#modularización...

def writing_wave (s_audio):
    """ Write the sine waves to a wave file. 
    The wave file is called 'sine_waves.wav'. 
    """

    s_audio = s_audio.tobytes()
    with wave.open('final.wav', 'w') as w:
        w.setnchannels(1)
        w.setsampwidth(2) 
        w.setframerate(frate) 
        w.setnframes(2) 
        w.writeframes(s_audio)
    

create_sine_each_note()
writing_wave (s_audio)

#crear wav y unirlos, la unica forma (con tiempo bien definido
# armonicos, array, ataque sostenido y decaimiento