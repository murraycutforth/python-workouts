def how_many_different_numbers(numbers):
    return len(set(numbers))


print(how_many_different_numbers([1, 2, 3, 1, 2, 3, 4, 1]))


from pathlib import Path

def file_exts():
    exts = set()
    for f in Path(".").glob("*"):
        if f.is_file():
            exts.add(f.suffix)
    print(exts)

file_exts()


