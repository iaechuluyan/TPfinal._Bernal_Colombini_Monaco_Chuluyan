**TPfinal._Bernal_Colombini_Monaco_Chuluyan
**
# Synthesizer

This repository contains a code that can transform song scores into wav files in a few seconds. The program receives two files, a score with all the notes of a song and their respective times and a list of harmonics and attack, sustain and decay functions that are used to make the sounds resemble real instruments. Also, this repository contains a small Python package that can communicate with a real xylophone.

## Libary of components:

- [Scripts](https://github.com/iaechuluyan/TPfinal._Bernal_Colombini_Monaco_Chuluyan/tree/main/scripts "Scripts")
- [xilophone](https://github.com/iaechuluyan/TPfinal._Bernal_Colombini_Monaco_Chuluyan/tree/main/xilophone "xiophone")
- [xilophone_execution](https://github.com/iaechuluyan/TPfinal._Bernal_Colombini_Monaco_Chuluyan/tree/main/xilophone_execution "xilophone_execution")

## General info
The folder called "scripts" contain the code referring to the first part of the task, that is, the music synthesizer. In addition to this, in this folder there are files that contain code that tests most of the functions that are used.
Then, the "xilophone_execution" folder contains all the necessary files for the user to be able to communicate with a real metallophone when entering a certain ip and connecting to a wifi network.
Last but not least, the "xilophone" folder contains other code referred to the communication with the real metallophone.
In order to use this library in another project it must be installed. Execute the following steps:
## Installation
1. Clone the repository 
```
$ git clone https://github.com/iaechuluyan/TPfinal._Bernal_Colombini_Monaco_Chuluyan.git
```
2. Get in the local repository
```
$ cd /path/to/the/sinthesizer
```
3. Install the dependencies
```
$ pip install -r requirements.txt
```
4. Install it with pip
```
$ pip install .
```
## Synthesizer Usage
First we'll show you how to call the synthesizer, pass a frequency, the file with the harmonics, a score and a name of the output file.
```python
cd scripts
```
```python
python main.py -f 44100 -h harmonics_p.txt -s example_song1.txt -o final.wav
```
## Testing
```python
cd scripts
```
```python
python test_function_to_test.py
```
## Communication with the real metallophone
The following steps are necessary to communicate with the real metallophone.
```python
cd xilophone_execution
```
Firstly, you need to run the python server that will be used to communicate with the real metallophone.
```python
python server.py
```
Then, you have to run the xylo_execution.py file.
```python
python xylo_execution.py -p example_song2.txt -d "10.42.0.1"
```
In order for the keys to start moving, the user must connect their computer to the Wi-Fi network called "kitty"
## Team
 [Tiziano Martin Bernal ](https://github.com/tizianomartinbernal)
 
 [Iael Chuluyan](https://github.com/iaechuluyan)
 
 [Romanella Colombini](https://github.com/Romanellac)
 
 [Vianca Monaco](https://github.com/vmonaco2)

## License

The MIT License (MIT)
