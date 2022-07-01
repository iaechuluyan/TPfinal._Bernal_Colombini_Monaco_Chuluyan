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
    def __init__(self, start, duration, amplitude, frequency, modulation_info, s_audio, frate):
        self.start = start
        self.end = duration + start
        self.frequency = frequency
        self.amplitude = amplitude
        self.modulation_info = modulation_info
        self.note_duration = duration
        self.frate = frate

        t = np.linspace(self.start, self.end, int((self.end-self.start)*self.frate)) 
        self.sine =  self.amplitude * np.sin(2* np.pi * self.frequency * t) 


    def sum_sine (self, sin):
        self.sine = sum([self.sine, sin.get_data()])


    def a_s_d (self, frate): 
        attack_end = (self.note_duration)*float(self.modulation_info[0][1])
        attack_step = int(attack_end*frate)

        decay_lasting = self.note_duration*float(self.modulation_info[2][1])
        decay_step = int(((self.note_duration)*float(self.modulation_info[2][1]))*frate)
        sustain_step = int((self.note_duration*frate) - attack_step - decay_step)

        attack_time = np.linspace(0, attack_end, attack_step)  
        sustain_time = np.linspace(attack_end, self.end - decay_lasting, sustain_step)
        decay_time = np.linspace(0,(self.note_duration)*float(self.modulation_info[2][1]), decay_step)

        #attack 
        A = F.func_linear(attack_time, attack_end)

        #sustain 
        S_total_time = self.note_duration - attack_end - (self.note_duration)*float(self.modulation_info[2][1])
        S = F.func_constant(sustain_time)
        #S = Sustain.invlog(sustain_time, S_total_time)
        #S = Sustain.pulses(sustain_time, S_total_time, 1, 2)

        #decay 
        D_total_time = (self.note_duration)*float(self.modulation_info[2][1])
        decay_start= (self.end - decay_lasting)
        D = F.func_invlinear(decay_time, D_total_time)

        M = np.concatenate((A, S, D))
        print(M)
        
        self.sine = np.multiply(self.sine, M)
    
    def translate_to_same_size (self, s_audio):
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

#v 1/07/22