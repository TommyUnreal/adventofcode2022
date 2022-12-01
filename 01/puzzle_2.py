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

def top_n_elves_total_calories(elves: list, no_elves: int) -> int:
    """"Remove elf with highest total_calories from array.

    Args:
        elves (list): List of Elf().
        no_elves (int): Number of how many top total_calories you want return.

    Returns:
        int: Sum of total_calories from no_elves elves.
    """
    total_calories = 0

    for _ in range(no_elves):
        maxed_elf = max(elves)
        total_calories += maxed_elf.total_calories
        elves.remove(maxed_elf)
    
    return total_calories

elves = [Elf()]

if __name__ == "__main__":
    with open(os.path.join(__location__,"input.txt")) as file:
        lines = [line for line in (l.strip() for l in file)]
        for input_line in lines:       
            if input_line.isdigit():
                elves[-1].total_calories += int(input_line)
            else:
                elves.append(Elf())

print(top_n_elves_total_calories(elves, 3))