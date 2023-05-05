def pl_word(word: str) -> str:
    if word[0] in "aeiou":
        return word + "way"
    else:
        return word[1:] + word[0] + "ay"

def pl_sentence(sent: str) -> str:
    words_translated = list(map(pl_word, sent.split()))
    return " ".join(words_translated)


print(pl_sentence("this is a test translation"))


# Beyond the exercise - string transposition

import itertools

def str_transposition(list_of_str: list) -> list:
    # List of N strings each containing N words
    n = len(list_of_str)
    assert all(len(x.split()) == n for x in list_of_str)

    flattened = list(itertools.chain(*[x.split() for x in list_of_str]))
    output = [" ".join(flattened[i::n]) for i in range(n)]
    return output

print(str_transposition(["abc def ghi", "jkl mno pqr", "stu vwx yz"]))


