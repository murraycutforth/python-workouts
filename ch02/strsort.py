def strsort(text: str) -> str:
    return "".join(sorted(text))

print(strsort("cba"))


def wordsort(text: str) -> str:
    words = text.split()
    return ",".join(sorted(words))

print(wordsort("Tom Dick Harry"))


def lastword(path: str) -> str:
    with open(path, "r") as infile:
        text = infile.read()
    words = text.split()
    return sorted(words)[-1]

print(lastword("text.txt"))


def longestword(path: str) -> str:
    with open(path, "r") as infile:
        text = infile.read()
    words = text.split()
    return sorted(words, key=lambda x: len(x))[-1]

print(longestword("text.txt"))
    

