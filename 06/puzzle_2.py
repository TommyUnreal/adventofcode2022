import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

if __name__ == "__main__":
    with open(os.path.join(__location__,"input.txt")) as file:
        lines = [line for line in file]

        n = 14
        for line in lines:
            for i in range(len(line)-n):
                test_set = set(line[i:i+n])
                if len(test_set) == n:
                    print(i+n)
                    break
