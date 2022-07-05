import argparse
from wavee import main

parser = argparse.ArgumentParser(description="Execute the python synthesizer")
parser.add_argument("-f", "--frequency", action="store" ,
default=48000, type=int, help="Sample rate", choices= [8000, 9600, 11025, 12000,
16000, 22050, 24000, 32000, 44100, 48000, 88200, 96000])
parser.add_argument("-i", "--instrument", action="store",
help="File with armonics and functions for attack, sustain and decay",
type = str)
parser.add_argument("-p", "--score",type=str, action="store",
help="File with the notes and the duration of each one")
parser.add_argument("-o","--wav" ,action = "store",type=str,
default="wavfile.wav", help="Name of the wav file to generate")
args = parser.parse_args()
frequency = args.frequency
instrument = args.instrument
score = args.score
wavfile = args.wav
main(frequency, instrument, score, wavfile)

