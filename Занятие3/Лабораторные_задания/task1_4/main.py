INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE, "r") as i:
        with open(OUTPUT_FILE, "w") as z:
            for upper_line in map(str.upper, i):
                z.write(upper_line)


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
