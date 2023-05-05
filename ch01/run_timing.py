from statistics import mean


def run_timing():
    times = []

    while True:
        t = input("Enter 10km run time: ")

        if t == "":
            break

        try:
            times.append(float(t))
        except ValueError:
            print("Invalid time")

    avg = mean(times)
    print(f"Average of {avg:.2f}, over {len(times)} runs")


run_timing()




