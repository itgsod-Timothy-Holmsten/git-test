lista = [5,1,6,8,9,0,3]

def insertion_sort(_list):
    for i in range(1, len(_list)):
        save = _list[i]
        j = i
        while j > 0 and _list[j-1] > save:
            _list[j] = _list[j-1]
            j -= 1
        _list[j] = save