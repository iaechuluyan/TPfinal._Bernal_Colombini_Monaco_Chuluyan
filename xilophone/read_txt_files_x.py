from notes import notes_mapping

def music_sheet_x (file):
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
            if info[0].startswith('.'):
                starts = 0.5
            else:
                starts = (info[0])
            
            note = info[1]

            line_info.append([starts, note])

    return line_info

def sorting_notes(notes):
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