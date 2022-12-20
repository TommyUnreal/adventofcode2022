import os
from collections import deque

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def get_first_element(lst):
    """Return the first element of iterable."""
    return lst[0]

if __name__ == "__main__":
    with open(os.path.join(__location__,"input.txt")) as file:
        lines = [int(line) for line in (l.strip() for l in file)]
        # deque list-like container with fast appends and pops on either end
        position_list  = deque([(value, index) for index, value in enumerate(lines)])

        # mixing
        for i, num in enumerate(lines):
            index = position_list.index((num, i))
            position_list.remove((num, i))
            #rotate the deque n steps to right
            position_list.rotate(-num)
            position_list.insert(index, (num, i))

        mixed_file = list(map(get_first_element, position_list))
        print(sum(mixed_file[(mixed_file.index(0)+1000*i) % len(lines)] for i in range(1,4)))