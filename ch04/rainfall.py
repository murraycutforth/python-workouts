from collections import defaultdict


def get_rainfall():
    rain_records = defaultdict(int)

    while True:
        city = input("Enter city name: ")

        if not city:
            break

        rainfall = int(input("Enter rainfall: "))

        rain_records[city] += rainfall

    print(rain_records)


get_rainfall()




