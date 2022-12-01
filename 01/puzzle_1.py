import os
from dataclasses import dataclass

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

@dataclass
class Elf():
    """Class for keeping track of elf and it's in inventory."""
    total_calories: int = 0

    def __lt__(self, other):
        """Overload < operator for comparing elves."""
        return self.total_calories < other.total_calories

elves = [Elf()]

if __name__ == "__main__":
    with open(os.path.join(__location__,"input.txt")) as file:
        lines = [line for line in (l.strip() for l in file)]
        for input_line in lines:       
            if input_line.isdigit():
                elves[-1].total_calories += int(input_line)
            else:
                elves.append(Elf())

print(max(elves))