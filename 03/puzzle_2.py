import os
from dataclasses import dataclass
from itertools import zip_longest

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

@dataclass
class Elf():
    """Dataclass for keeping track of single elf and it's rucksack."""
    rucksack: set

class ElfGroup():
    """Class for keeping track of elf groups."""

    def __init__(self, elves) -> None:
        """Initialize Elf object.

        Args:
            elves (list): List of elves belonging to the group.
        """
        self.elves = elves

    def check_inventory(self):
        """Find and store badge item in badge item attribute.
        
        badge_item represents items stored across all elves in the ElfGroup object.
        """
        self.badge_item = list(set.intersection(*[item.rucksack for item in self.elves]))
        self.compute_value()

    def compute_value(self):
        """Compute value of badge item based on priority.
        
        Lowercase item types a through z have priorities 1 through 26.
        Uppercase item types A through Z have priorities 27 through 52.
        """
        self.badge_item_value = 0
        for item in self.badge_item:
            self.badge_item_value += (ord(item) - 64)%32 + item.isupper()*26

    def __radd__(self, other):
        """Override summing of ElfGroup object to sum badge item value.

        Args:
            other (ElfGroup): ElfGroup object to be added to the sum.

        Returns:
            _type_: Summed ElfGroup object.
        """
        return other + self.badge_item_value

def group_list(n, iterable:list) -> list:
    """Group list to list of tuples of size n.

    Args:
        n (int): Size of output groups.
        iterable (list): List to be grouped.

    Returns:
        list: List of groups (tuples).
    """
    args = [iter(iterable)] * n
    return list(zip_longest(*args))

elf_groups = []
group_size = 3

if __name__ == "__main__":
    with open(os.path.join(__location__,"input.txt")) as file:
        lines = [line for line in (l.strip() for l in file)]
        grouped_lines = group_list(group_size, lines)

        for input_lines in grouped_lines:
            queued_elves = []

            for single_line in input_lines:
                elf = Elf(set(single_line))
                queued_elves.append(elf)
            
            elf_group = ElfGroup(queued_elves)
            elf_group.check_inventory()
            elf_groups.append(elf_group)

print(sum(elf_groups))