from notes import notes_mapping

def music_sheet (file: str) -> list:
    '''
    Returns a list of lists with the starting time, the frequency and the lasting time of all the notes from
    the sheet file.

    Parameters
    ----------
        file : str
            The name of the file.
    Returns 
    -------
        line_info : list
            The list in question.

    '''
    line_info = []
    with open (file, 'r') as f:
        for line in f:
            info = line.split(' ')
            if info[0].startswith('.'):
                starts = 0.5
            else:
                starts = float(info[0])
            
            note = get_frequency(info[1])

            if info[2].startswith('.'):
                duration = 0.5
            else:
                duration = int(info[2])

            line_info.append([starts, note, duration])
    
    return line_info


def get_frequency (note: str) -> int:
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