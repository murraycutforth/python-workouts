from operator import itemgetter

PEOPLE = [("DONALD", "TRUMP", 7.85), ("VLADIMIR", "PUTIN", 3.626), ("JINPING", "XI", 10.603)]

def format_sort_records():
    output = ""
    for record in sorted(PEOPLE, key=itemgetter(1, 0)):
        output += f"{record[1]:10} {record[0]:10} {record[2]:5.2f}\n"
    return output


print(format_sort_records())

