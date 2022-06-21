from re import I
import wave
import numpy as np
import math
import matplotlib.pyplot as plt
import contextlib
from read_txt_files import music_sheet_info 

frate = 44100
s_audio = np.array([], 'int16')

class sine:
    def __init__(self, start, duration, frequency, i):
        global s_audio
        self.start = start
        self.duration = duration
        self.frequency = frequency
        self.amplitude = 0.5
        self.i = i
        t = np.arange(self.start, self.duration, 0.00001) 
        sine =  self.amplitude * np.sin(2* np.pi * self.frequency * t) #numeros menores a un segundo
        self.sine = (sine * (2 ** 15 - 1)).astype("<h")
        np.concatenate(s_audio, self.sine) #

        #clase seno, agarramos y vamos concatenando los arrays, los de to bytes (con get data), 
        #ese array grande lo metemos todo en el wav file y listooo
        # superpuestas: videos de yt del italiano

    def get_data (self):
        return self.sine

    def __repr__(self):
        return self.i

    def __str__(self):
        return str(self.i)

def create_sine_each_note ():
    i = 0
    for note in music_sheet_info:
        S = sine (note[0], note[2], note[1], i)
        i+=1



def writing_wave (s_audio):
    s_audio = s_audio.tobytes()
    with wave.open('final.wav', 'w') as w:
        w.setnchannels(1)
        w.setsampwidth(2) 
        w.setframerate(frate) 
        w.setnframes(2) 
        w.writeframes(s_audio)
    

# def union_of_wav (wav_list):
#     #uno sus wavs
#     union = "final.wav"

#     data= []
#     for wav in wav_list:
#         w = wave.open(wav, 'rb')
#         data.append( [w.getparams(), w.readframes(w.getnframes())] )
#         w.close()
    
#     output = wave.open(union, 'wb')
#     output.setparams(data[0][0])
#     for i in range(len(data)):
#         output.writeframes(data[i][1])
#     output.close()


    #elimino los otros wavs de la lista?
    #manejar el tema de los tiempos, overlapping


create_sine_each_note()
writing_wave (s_audio)






#crear wav y unirlos, la unica forma (con tiempo bien definido
# armonicos, array, ataque sostenido y decaimiento