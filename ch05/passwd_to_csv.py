import csv
from collections import namedtuple


def passwd_to_csv():
    PasswdRow = namedtuple("PasswdRow", ["user", "userid"])
    all_rows = []

    with open("/etc/passwd") as infile:
        reader = csv.reader(infile, delimiter=":")
        for row in reader:
            all_rows.append(PasswdRow(user=row[0], userid=row[2]))

    with open("user_and_id.csv", "w") as outfile:
        writer = csv.writer(outfile, delimiter="\t")
        for row in all_rows:
            writer.writerow(row)


passwd_to_csv()

