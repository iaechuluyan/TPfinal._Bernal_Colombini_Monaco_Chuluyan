from notes import notes_mapping

def sorting_notes(notes):
    if type(notes) != list:
        raise TypeError('notes must be a list')
    if len(notes) == 0:
        raise ValueError('list must be of length different than 0')

    # for i in range(0, len(notes)):
    #     if type(notes[i]) != list:
    #         raise TypeError()



    if len(notes) > 1:
        r = len(notes) // 2
        L = notes[:r]
        M = notes[r:]

        sorting_notes(L)
        sorting_notes(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i][0] < M[j][0]:
                notes[k] = L[i]
                i+=1
            else:
                notes[k] = M[j]
                j+=1
            k+=1


        while i < len(L):
            notes[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            notes[k] = M[j]
            j += 1
            k += 1

    return notes

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
    if 'txt' not in file:
        raise TypeError('file must be a txt file')

    line_info = []
    with open (file, 'r') as f:
        for line in f:
            line.strip('\n')
            info = line.split(' ')
            if info[0].startswith('.'):
                starts = 0.5
            else:
                starts = float(info[0])
            
            note = get_frequency(info[1])

            if info[2].startswith('.'):
                duration = 0.5
            else:
                duration = float(info[2])
            line_info.append([starts, note, duration])

    line_info = sorting_notes(line_info)
    
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
    if type(note) != str:
        raise TypeError('note must be a string')

    for tuple in notes_mapping:
        if note == tuple[0]:
            return tuple[1]
        else:
            continue

def harmonics_info (file):
    '''
    Returns two lists, one with the information of each harmonic read in a file and another one with
    the information of which functions to use (along with it's arguments) for attack, sustain, and decay.

    Parameters
    ----------
    file : txt file
        file containing the harmonics.

    Returns
    -------
        Two lists.
    
    '''
    if 'txt' not in file:
        raise TypeError('file must be a txt file')

    with open(file, 'r') as f:
        i = 0
        lines = f.readlines()
        length = len(lines)
        harmonic_info = []
        A_S_D = []

        while i < length:
            if i == 0:
                i+=1
            elif i >0 and i < length - 3:
                lines[i] = lines[i][:-1]
                harmonic_info.append(lines[i].split(' '))
                i+=1
            elif i == length -1:
                A_S_D.append(lines[i].split(' '))
                i+=1
            else:
                lines[i] = lines[i][:-1]
                A_S_D.append(lines[i].split(' '))
                i+=1

        harmonics_info= sorting_harmonics(harmonic_info)

    list_h_a_s_d = [harmonics_info, A_S_D]
    
    return list_h_a_s_d

def sorting_harmonics(harmonics):
    '''
    Orders the list of harmonics.

    Parameters
    ----------
    harmonics : list
        Contains the harmonics' information.

    Returns
    -------
        The harmonics' list ordered.
    
    '''
    if type(harmonics) != list:
        raise TypeError('harmonics must be a list')
    if len(harmonics) == 0:
        raise ValueError('list must be of length different than 0')
    

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


