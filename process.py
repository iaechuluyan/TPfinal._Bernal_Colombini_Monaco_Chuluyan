import numpy as np
from a_s_d_functions import Attack, Sustain, Decay
from read_txt_files import modulation_info

Attack = Attack()
Sustain = Sustain()
Decay = Decay()

class process: 
    '''


    '''
    def __init__(self, start, duration, amplitude, frequency, h, frate):
        self.start = start
        self.duration = duration 
        self.frequency = frequency
        self.amplitude = amplitude

        t = np.linspace(self.start, self.duration, frate) 
        self.sine =  self.amplitude * np.sin(2* np.pi * self.frequency * t) 
        
        self.len = self.sine.shape[0]


    def sum_sine (self, sin):
        self.sine = sum([self.sine, sin.get_data()])


    def modularizar (self, frate): 
        M = np.zeros(self.len)

        note_duration = self.duration-self.start

        attack_step = int(((note_duration*float(modulation_info[0][1]))*frate))
        decay_step = int(((note_duration) - ((note_duration) - ((note_duration)*float(modulation_info[2][1]))))*frate)
        
        if decay_step < attack_step:
            sustain_step = (note_duration)*frate - attack_step - decay_step 
        else:
            sustain_step = (note_duration)*frate - decay_step - attack_step



        #del cero hasta lo que duran, sino, pruebo del cero al uno?, mm no, no?
        attack_time = np.linspace(0, ((note_duration)*float(modulation_info[0][1])), attack_step)  
        sustain_time = np.linspace((note_duration)*float(modulation_info[0][1]), self.duration - (self.duration*float(modulation_info[2][1])), sustain_step)
        decay_time = np.linspace((note_duration) - ((note_duration)*float(modulation_info[2][1])), self.duration, decay_step)




        #attack
        A_total_time = (note_duration)*float(modulation_info[0][1])
        A = Attack.func_linear(attack_time, A_total_time)
        for a in range(0,len(A)):
            M[a] = A[a]

        #sustain
        S_total_time = note_duration - (note_duration)*float(modulation_info[0][1]) - (note_duration)*float(modulation_info[2][1])
        #S = Sustain.func_constant(sustain_time)
        #S = Sustain.invlog(sustain_time, S_total_time)
        S = Sustain.pulses(sustain_time, S_total_time, 1, 2)
        for m, s in zip(range(len(A), len(S)+len(A)), range(0, len(S))):
            M[m] = S[s] 

        #decay
        D_total_time = (note_duration)*float(modulation_info[2][1])
        decay_start= (self.duration - self.duration*float(modulation_info[2][1]))
        D = Sustain.func_invlinear(decay_time, D_total_time, decay_start)
        for m, d in zip(range(len(S)+len(A) , len(D)+len(S)+len(A)), range(0,len(D))):
            M[m] = D[d]

        
        self.sine = np.multiply(self.sine, M)

    def size(self):
        return len(self.sine)


    def get_data (self):
        return self.sine

    def __repr__(self):
        return self.i

    def __str__(self):
        return str(self.i)