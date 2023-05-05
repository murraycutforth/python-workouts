from collections import Counter

def most_repeating_word(seq):
    current_max = -1
    current_result = None

    for word in seq:
        counts = Counter(word)
        this_max = max(counts.values())

        if this_max > current_max:
            current_max = this_max
            current_result = word

    return current_result


print(most_repeating_word(["this", "is", "an", "elementary", "test", "example"]))
        

# Better solution

def max_letter_count(word):
    return Counter(word).most_common(1)[0][1]

def most_repeating_word(seq):
    return max(seq, key=max_letter_count)

print(most_repeating_word(["this", "is", "an", "elementary", "test", "example"]))
