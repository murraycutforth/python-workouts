def wordcount(filename):
    lines = 0
    chars = 0
    words = 0
    unique_words = set()

    with open(filename) as infile:
        for line in infile:
            lines += 1
            chars += len(line)

            for word in line.split():
                words += 1
                unique_words.add(word)

    print(f"Number of chars (incl whitespace): {chars}")
    print(f"Number of words: {words}")
    print(f"Number of unique words: {len(unique_words)}")
    print(f"Number of lines: {lines}")
                
                
wordcount("test.txt")
