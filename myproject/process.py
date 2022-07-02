import numpy as np
from a_s_d_functions import Functions

F= Functions()

class process: 
    '''
    This class is used to create a note.

    Attributes:
    ----------
    start (float): The time the note starts.
    end (float): The time the note ends.
    frequency (float): The frequency of the note.
    amplitude (float): The amplitude of the note.
    modulation_info (float): The modulation info of the note.
    note_duration (float): The duration of the note.
    sine (numpy array): The sine wave of the note.
    len (int): The length of the sine wave.

    Methods:
    --------
    sum_sine (self, sin): Sums the numpy arrays of the note with the
    numpy array of the note.
    size (self): Returns the length of the sine wave.
    get_data (self): Returns the sine wave.

    '''
    def __init__(self, start, duration, amplitude, frequency, modulation_info, frate):
        if type(start) not in [int, float] or type(duration) not in [int, float] or type(amplitude) not in [int, float] or type(frequency) not in [int, float]:
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

        self.dict = { "LINEAR" : F.func_linear, "EXP": F.exp, "QUARTSIN" : F.quartsin , "HALFSIN" : F.halfsin , "LOG" : F.log , "TRI" : F.tri, "CONSTANT" : F.func_constant , 
    "INVLINEAR" : F.func_invlinear, "SIN" : F.func_sin , "INVEXP" : F.invexp , "QUARTCOS" : F.quartcos , "INVLOG" : F.invlog, "PULSES" : F.pulses , "QUARTCOS" : F.quartcos ,
    "HALFCOS" : F.halfcos}

    def decide_function(self, a_time, a_end, s_time, s_tot_time, d_time, d_tot_time):
        if type(a_time) != type(np.array(0)) or type(s_time)!= type(np.array(0)) or type(d_time)!= type(np.array(0)):#asi se dice el type?
            raise TypeError('a_time, s_time and d_time must be numpy arrays')
        if type(a_end) not in [int, float] or type(s_tot_time) in [int, float] or type(d_tot_time) in [int, float]:
            raise TypeError('a_time, s_time, d_time must be of type int or float')

        if self.modulation_info[0][0] in ['TRI']:
            a= self.dict[self.modulation_info[0][0]](a_time, a_end, self.modulation_info[0][2], self.modulation_info[0][3])
        else:
            a = self.dict[self.modulation_info[0][0]](a_time, a_end)

        if self.modulation_info[1][0] in ['CONSTANT']:
            s = self.dict[self.modulation_info[1][0]](s_time)
        elif self.modulation_info[1][0] in ['SIN', 'PULSES']:
            s = self.dict[self.modulation_info[1][0]](d_time, d_tot_time, self.modulation_info[1][2], self.modulation_info[1][3])
        else:
            s = self.dict[self.modulation_info[1][0]](s_time, s_tot_time)

        d = self.dict[self.modulation_info[2][0]](d_time, d_tot_time)


        return a, s, d


    def sum_sine (self, sin):
        if isinstance(sin, process):
            self.sine = sum([self.sine, sin.get_data()])
        else:
            raise TypeError("sin must be a process class' object")

    def a_s_d (self, frate): 
        if type(frate) != int:
            raise ValueError('frate must be a variable of int type')


        attack_end = (self.note_duration)*float(self.modulation_info[0][1])
        attack_step = int(attack_end*frate)

        decay_lasting = self.note_duration*float(self.modulation_info[2][1])
        decay_step = int(((self.note_duration)*float(self.modulation_info[2][1]))*frate)
        sustain_step = int((self.note_duration*frate) - attack_step - decay_step)

        attack_time = np.linspace(0, attack_end, attack_step)  
        sustain_time = np.linspace(attack_end, self.end - decay_lasting, sustain_step)
        decay_time = np.linspace(0,(self.note_duration)*float(self.modulation_info[2][1]), decay_step)

        S_total_time = self.note_duration - attack_end - (self.note_duration)*float(self.modulation_info[2][1])
        D_total_time = (self.note_duration)*float(self.modulation_info[2][1])


        A, S, D = self.decide_function(attack_time, attack_end, sustain_time, S_total_time, decay_time, D_total_time)

        M = np.concatenate((A, S, D))
        print(M)
        
        self.sine = np.multiply(self.sine, M)
    
    def translate_to_same_size (self, s_audio):
        if type(s_audio) != type(np.array(0)):  #asi se dice el type?
            raise TypeError('s_audio must be a numpy array')

        conc1 = np.zeros(int(self.start*self.frate)) 
        self.sine = np.concatenate((conc1,self.sine)) 
        aux_calc = len(s_audio)-len(self.sine)
        conc2 = np.zeros (aux_calc)
        self.sine = np.concatenate((self.sine, conc2))

    def size(self):
        return len(self.sine)

    def get_data (self):
        return self.sine

    def __repr__(self):
        return self.i

    def __str__(self):
        return str(self.i)
