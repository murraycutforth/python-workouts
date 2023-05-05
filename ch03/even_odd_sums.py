def even_odd_sums(seq):
    return [sum(seq[::2]), sum(seq[1::2])]


print(even_odd_sums([10, 20, 30, 40, 50, 60]))
