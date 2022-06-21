from re import L
from notes import notes_mapping



def music_sheet (file):
    '''
    Returns a list of lists with the starting time, the frequency and the lasting time of all the notes from
    the sheet file.

    Parameters
    ----------
        file : file

    Returns 
    -------
        line_info : list
            The list in question.

    '''
    line_info = []
    with open (file, 'r') as f:
        for line in f:
            line.strip('\n')
            info = line.split(' ')
            print(info)
            print('0: ', info[0], '1: ', info[1], '2: ', info[2])
            if info[0].startswith('.'):
                starts = 0.5
            else:
                starts = int(info[0])
            
            note = get_frequency(info[1])

            if info[2].startswith('.'):
                duration = 0.5
            else:
                duration = int(info[2])
            print('arrived')
            line_info.append([starts, note, duration])

    
    
    return line_info


def get_frequency (note):
    '''
    Returns the frequency of a given note by searching it on a list of tuples.

    Parameters
    ----------
    note : str
        The note in question.

    Returns
    -------
        The frequency related to the note.
    
    '''
    for tuple in notes_mapping:
        if note == tuple[0]:
            return tuple[1]
        else:
            continue

def harmonics_info (file):
    with open(file, 'r') as f:
        i = 0
        length = f.readlines()
        harmonic_info = []
        A_S_D = []
        while i < len(length):
            line = f.readline()
            if i == 0:
                i+=1
            elif i >0 and i < len(length) - 3:
                harmonic_info.append(line.split(' '))
    
            else:
                A_S_D.append(line.split(' '))

        sorting_harmonics(harmonic_info)
    
    print(harmonics_info)
    return harmonics_info

music_sheet_info =  music_sheet ('example.txt')  
harmonics_info = (harmonics_info('piano.txt'))

def sorting_harmonics(harmonics):
    if len(harmonics) > 1:
        r = len(harmonics) // 2
        L = harmonics[:r]
        M = harmonics[r:]

        sorting_harmonics(L)
        sorting_harmonics(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i][0] < M[i][0]:
                harmonics[k] = L[i]
                i+=1
            else:
                harmonics[k] = M[j]
                j+=1
            k+=1


        while i < len(L):
            harmonics[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            harmonics[k] = M[j]
            j += 1
            k += 1

    return harmonics




#sort de las notas, algoritmo para añadirlas