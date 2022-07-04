import wave
import numpy as np
from read_txt_files import music_sheet, harmonics_info
from process import process as sinthesizer
from plot_file import plot

def main(frate, h_file, p_file, wavfile):
    if type(frate) != int:
        raise TypeError('Only integers allowed')
    if 'txt' not in h_file or 'txt' not in p_file:
        raise TypeError('h_file and p_file must be txt files')
    if 'wav' not in wavfile:
        raise TypeError('wavfile must be a wav file')
    

    music_sheet_info = music_sheet (p_file) 
    harmonic_info, modulation_info = harmonics_info(h_file)
    length = music_sheet_info[-1][0] + music_sheet_info[-1][2]
    s_audio = np.zeros(int(length * frate))
    s_audio = create_sine_each_note (s_audio, harmonic_info, music_sheet_info, modulation_info, length, frate)
    writing_wave(s_audio, wavfile, frate)

def writing_wave (s_audio, wavfile,frate = 44100):
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
    if type(s_audio) != type(np.array(0)):  
        raise TypeError('s_audio must be a numpy array')
    if type(frate) != int:
        raise TypeError('Only integers allowed')
    if 'wav' not in wavfile:
        raise TypeError('wavfile must be a wav file')


    s_audio = (s_audio*300).astype('<h')
    s_audio = s_audio.tobytes()
    with wave.open(wavfile, 'w') as w:
        w.setnchannels(1)
        w.setsampwidth(2) 
        w.setframerate(frate) 
        w.setnframes(2) 
        w.writeframes(s_audio)

def create_sine_each_note (s_audio, harmonic_info, music_sheet_info, modulation_info, length, frate = 44100):
    '''
    Iterates over the list of notes and harmonics in order to append the data to the main numpy array (s_audio)
    Uses the process class methods to apply attack, sustain and decay and translate the created numpy array to 
    the same size as the main numpy array in order to sum them.

    Parameters
    ----------
        s_audio : empty list
        harmonic_info : list containing the information related to the harmonics.
        music_sheet_info : list containing the information related to the music notes.
        modulation_info : list containing the information related to the attack, decay and sustain.
        length : the length in seconds of the song.
        frate : frame rate

    Returns 
    -------
        s_audio : numpy array (The array with the appended data)

    '''
    if type(s_audio) != type(np.array(0)):  
        raise TypeError('s_audio must be a numpy array')
    if len(s_audio) != int(length * frate):
        raise Exception('the length of the file is not the correct one')
    if type(harmonic_info) != list or type(music_sheet_info) != list or type(modulation_info) != list:
        raise TypeError('harmonic_info, music_sheet_info and modulation_info must be of type list')
    if len(harmonic_info) == 0 or len(music_sheet_info) == 0 or len(modulation_info) == 0:
        raise ValueError('list must be of length different than 0')


    for note in music_sheet_info:
        h = []
        for frequency_change, amplitude in (harmonic_info):
            S = sinthesizer(note[0], note[2], float(amplitude), float(note[1] * float(frequency_change)), modulation_info,frate) 
            if type(h) is not list:
                h.sum_sine(S)
            else:
                h = S


        h.a_s_d(frate)
        h.translate_to_same_size(s_audio)

        note_info = h.get_data() 

        s_audio += note_info  

    return s_audio

main(44100, 'harmonics.txt', 'queen.txt', 'wav.wav')
plot()