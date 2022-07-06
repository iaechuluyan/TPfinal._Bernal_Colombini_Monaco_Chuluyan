import numpy as np
from a_s_d_functions import Functions
import math
F= Functions()

class Process: 
    '''
    This class is used to create a note.

    Attributes:
    ----------
    start (float): The time the note starts.

    end (float): The time the note ends.

    frequency (float): The frequency of the note.

    amplitude (int): The amplitude of the note.

    modulation_info (list): list containing the attack, sustain, and decay information.

    note_duration (float): The duration of the note.

    sine (numpy array): The numpy array with the values the sine wave of
    the note would take.

    frate: the given frequency rate.

    dict: the dictionary containing the functions to use for attack, sustain and decay.

    Methods:
    --------
    decide_function (self, a_time, a_end, s_time, s_tot_time, d_time, d_tot_time):
    uses a dictionary to interpret which attack, sustain and decay function
    to use depending on the ones specified on the harmonics text file.

    sum_sine (self, sin): Sums the numpy arrays of the note with the
    numpy array of some other note.

    a_s_d (self, frate): applies the attack, sustain, and decay modulation to the note.

    set (self, s_audio): adds the note to the main numpy array (s_audio)
    at the correct position.

    size (self): Returns the length of the sine wave.

    get_data (self): Returns self.sine

    '''
    def __init__(self, start, duration, amplitude, frequency, modulation_info, frate):
        if str(type(start)) not in ["<class 'int'>",
        "<class 'float'>"] or str(type(duration)) not in ["<class 'int'>",
        "<class 'float'>"] or str(type(amplitude)) not in ["<class 'int'>",
        "<class 'float'>"] or str(type(frequency)) not in ["<class 'int'>",
        "<class 'float'>"]:
            raise ValueError('must be of integer or float type') 
        if type(modulation_info) != list:
            raise TypeError('modulation_info must be a list')
        if len(modulation_info) == 0:
            raise ValueError('list must be of length different than 0')
        if type(frate) != int:
            raise ValueError('frate must be a variable of int type')

        self.start = start
        self.note_duration = duration
        self.end = duration + start
        self.frequency = frequency
        self.amplitude = amplitude
        self.modulation_info = modulation_info
        self.frate = frate

        t = np.linspace(self.start, self.end, int((self.end-self.start)*self.frate)) 
        self.sine =  self.amplitude * np.sin(2* np.pi * self.frequency * t) 

        self.dict = { "LINEAR" : F.linear, "EXP": F.exp, "QUARTSIN" : F.quartsin
        , "HALFSIN" : F.halfsin , "LOG" : F.log , "TRI" : F.tri, "CONSTANT" : F.constant, 
    "INVLINEAR" : F.invlinear, "SIN" : F.sin , "INVEXP" : F.invexp ,
    "QUARTCOS" : F.quartcos , "INVLOG" : F.invlog, "PULSES" : F.pulses ,
    "QUARTCOS" : F.quartcos , "HALFCOS" : F.halfcos}

    def decide_function(self, a_time, a_end, s_time, s_tot_time, d_time, d_tot_time): 
        if type(a_time) != type(np.array(0)) or type(s_time)!= type(np.array(0)) or type(d_time)!= type(np.array(0)):
            raise TypeError('a_time, s_time and d_time must be numpy arrays')
        if type(a_end) != float or type(s_tot_time) != float or type(d_tot_time) != float:
            raise TypeError('a_time, s_time, d_time must be of type int or float')

        if self.modulation_info[0][0] in ['TRI']:
            a = self.dict[self.modulation_info[0][0]](a_time, a_end,
            float(self.modulation_info[0][2]), float(self.modulation_info[0][3]),
            self.frate)
        else:
            a = self.dict[self.modulation_info[0][0]](a_time, a_end)

        if self.modulation_info[1][0] in ['CONSTANT']:
            s = self.dict[self.modulation_info[1][0]](s_time)
        elif self.modulation_info[1][0] in ['SIN', 'PULSES']:
            s = self.dict[self.modulation_info[1][0]](s_time, s_tot_time,
            self.modulation_info[1][2], self.modulation_info[1][3])
        else:
            s = self.dict[self.modulation_info[1][0]](s_time, s_tot_time)

        d = self.dict[self.modulation_info[2][0]](d_time, d_tot_time)


        return a, s, d


    def sum_sine (self, sin):
        if isinstance(sin, Process):
            self.sine = sum([self.sine, sin.get_data()])
        else:
            raise TypeError("sin must be a process class' object")
        
    def a_s_d(self,frate):
        if type(frate) != int:
            raise ValueError('frate must be a variable of int type')
        if float(self.note_duration) == 0.0:
            pass
        else:
            attack_end = (self.note_duration)*float(self.modulation_info[0][1])
            attack_step = int(attack_end*frate)

            decay_lasting = self.note_duration*float(self.modulation_info[2][1])
            decay_step = int(decay_lasting*frate)
            sustain_step = int((self.note_duration*frate) - attack_step - decay_step)

            attack_time = np.linspace(0, attack_end, attack_step)  
            sustain_time = np.linspace(attack_end, self.end - decay_lasting, sustain_step)
            decay_time = np.linspace(0, decay_lasting, decay_step)

            part1 = self.note_duration - attack_end
            part2 = (self.note_duration)*float(self.modulation_info[2][1])
            S_total_time = part1 - part2
            D_total_time = (self.note_duration)*float(self.modulation_info[2][1])


            A, S, D = self.decide_function(attack_time, attack_end,
            sustain_time, S_total_time, decay_time, D_total_time)

            M = np.concatenate((A, S, D))

            
            self.sine = np.multiply(self.sine, M)

 
    
    def set (self, s_audio):
        if type(s_audio) != type(np.array(0)):  
            raise TypeError('s_audio must be a numpy array')

        s = int(self.start * self.frate)
        f= int(s + self.note_duration*self.frate)
        s_audio[s:f] = s_audio[s:f] + self.sine


    def size(self):
        return len(self.sine)

    def get_data (self):
        return self.sine

    def __repr__(self):
        return self.i

    def __str__(self):
        return str(self.i)
