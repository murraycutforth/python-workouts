from pathlib import Path


def word_generator(fileobj):
    for line in fileobj:
        for word in line.split():
            yield word


def find_longest_word(filename):
    with open(filename) as infile:
        longestword = max(word_generator(infile), key=len)
    return longestword


def find_all_longest_words(dirname):
    filenames = [x for x in Path(dirname).glob("*") if x.is_file()]
    return {x.name: find_longest_word(x) for x in filenames}


print(find_all_longest_words("."))


import hashlib


def get_md5_single_file(filename):
    with open(filename, "rb") as infile:
        md5hash = hashlib.md5(infile.read()).digest()
    return md5hash


def get_md5_hashes(dirname):
    filenames = [x for x in Path(dirname).glob("*") if x.is_file()]
    return {x.name: get_md5_single_file(x) for x in filenames} 


print(get_md5_hashes("."))

