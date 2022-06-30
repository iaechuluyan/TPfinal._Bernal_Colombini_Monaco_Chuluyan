
from re import A
import wave
import numpy as np
#import math
import matplotlib as mpl
import matplotlib.pyplot as plt
#import contextlib
from read_txt_files import music_sheet_info, harmonics_info
#import sys
from process import process as sinthesizer
from plot_file import plot

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
            S = sinthesizer(note[0], note[2], float(amplitude), float(note[1] * float(frequency_change)), h, frate)
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

main(frate=44100)
plot()



#