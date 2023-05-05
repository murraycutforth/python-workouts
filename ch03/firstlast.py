from operator import itemgetter

def firstlast(seq):
    # Will fail on empty sequence
    return seq[::max(1, len(seq) - 1)]

    # Incorrect for len == 1
    #return itemgetter(0, -1)(seq)


print(firstlast("a"))
print(firstlast("ab"))
print(firstlast("abc"))
print(firstlast([1, 2, 3, 4]))
