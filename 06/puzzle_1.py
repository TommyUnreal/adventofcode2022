import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

if __name__ == "__main__":
    with open(os.path.join(__location__,"input.txt")) as file:
        lines = [line for line in file]

        for line in lines:
            for i in range(len(line)-4):
                test_set = set(line[i:i+4])
                if len(test_set) == 4:
                    print(i+4)
                    break
