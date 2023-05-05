import string
from collections import defaultdict

def create_dict():
    return {char: i + 1 for i, char in enumerate(string.ascii_lowercase)}

CHAR_VALUE = create_dict()

def gematria_for(word):
    return sum(CHAR_VALUE.get(char, 0) for char in word.lower())

VAL_WORDS = defaultdict(list)
with open("words.txt") as infile:
    for line in infile:
        word = line.strip()
        val = gematria_for(word)
        VAL_WORDS[val].append(word)

def gematria_equal_words(word):
    return VAL_WORDS[gematria_for(word)]

print(create_dict())
print(gematria_for("a"))
print(gematria_for("z"))
print(gematria_for("murray"))
print(gematria_for("Alex"))
print(gematria_for("Liat"))
