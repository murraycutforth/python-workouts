def get_final_line(path):
    with open(path, "r") as infile:
        lines = infile.readlines()
    return lines[-1]

print(get_final_line("test.txt"), end="")


def sum_numbers(path):
    total = 0
    with open(path, "r") as infile:
        for line in infile:
            for word in line.split():
                try:
                    total += int(word)
                except ValueError:
                    pass
    return total

print(sum_numbers("test.txt"))


from collections import Counter
import re
import itertools

def count_vowels(path):
    with open(path, "r") as infile:
        key = lambda x: x in "aeiou"
        vowel_counts = Counter(filter(key, itertools.chain(*infile)))

    return vowel_counts

print(count_vowels("test.txt"))
            
            

    
