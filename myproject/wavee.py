import wave
import numpy as np
from read_txt_files import music_sheet, harmonics_info
from process import process as sinthesizer
from plot_file import plot

def main(frate, h_file, p_file, wavfile):
    music_sheet_info = music_sheet (p_file) 
    harmonic_info, modulation_info = harmonics_info(h_file)
    l = music_sheet_info[-1][0]
    e= music_sheet_info[-1][2]
    length = l+e
    s_audio = np.zeros(int(length * frate))
    writing_wave (create_sine_each_note(s_audio, harmonic_info, music_sheet_info, modulation_info, frate), wavfile, frate)

def writing_wave (s_audio, wavfile, frate = 44100):
    '''
    Writes the data on the wav file.

    Parameters
    ----------
        s_audio : numpy array
        wavfile: wav binary file
        frate : frame rate

    Returns 
    -------
        None

    '''
    s_audio = (s_audio*300).astype('<h')
    s_audio = s_audio.tobytes()
    with wave.open(wavfile, 'w') as w:
        w.setnchannels(1)
        w.setsampwidth(2) 
        w.setframerate(frate) 
        w.setnframes(2) 
        w.writeframes(s_audio)


def create_sine_each_note (s_audio, harmonic_info, music_sheet_info, modulation_info, frate = 44100):
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
        for frequency_change, amplitude in (harmonic_info):
            S = sinthesizer(note[0], note[2], float(amplitude), float(note[1] * float(frequency_change)), modulation_info, s_audio, frate)
            if type(h) is not list:
                h.sum_sine(S)
            else:
                h = S

        
        # starting_i = int(h.start * frate)
        # until_i = int((h.end) * frate)

        h.a_s_d(frate)
        h.translate_to_same_size(s_audio)

        note_info = h.get_data() 

        s_audio += note_info  

    return s_audio

main(44100, 'harmonics.txt', 'queen.txt', 'wav.wav')
plot()
