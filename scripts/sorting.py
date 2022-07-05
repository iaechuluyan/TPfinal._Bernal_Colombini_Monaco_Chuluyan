def sorting_harmonics(array):
    """
    Used for the sorting of notes.

    Parameters
    ----------
        array : the list with the notes' information

    Returns
    -------
        array : the sorted list.
    
    """
    if type(array) != list:
        raise TypeError('array must be a list')
    if len(array) == 0:
        raise ValueError('list must be of length different than 0')

    if len(array) > 1:
        r = len(array) // 2
        L = array[:r]
        M = array[r:]

        sorting_harmonics(L)
        sorting_harmonics(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i][0] < M[j][0]:
                array[k] = L[i]
                i+=1
            else:
                array[k] = M[j]
                j+=1
            k+=1


        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

    return array


def sorting_notes (array):
    """
    Used for the sorting of notes.

    Parameters
    ----------
        array : the list with the notes' information

    Returns
    -------
        array : the sorted list.
    
    """
    if type(array) != list:
        raise TypeError('array must be a list')
    if len(array) == 0:
        raise ValueError('list must be of length different than 0')

    for each in range(len(array)):
        min_idx = each
        for i in range(each + 1, len(array)):
            if array[i][0]+array[i][2] < array[min_idx][2]+array[min_idx][2]:
                min_idx = i

        (array[each], array[min_idx]) = (array[min_idx], array[each])
    
    return array

