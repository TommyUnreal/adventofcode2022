import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

class Elf():
    """Class for keeping track of elf and it's in inventory."""

    def __init__(self, rucksack:str) -> None:
        """Initialize Elf object.

        Args:
            rucksack (str): Content of rucksack, one item per character.
        """
        self.rucksack = rucksack

    def check_inventory(self):
        """Find and store shared items in shared_items attribute.
        
        shared_items represents items stored both in first half and second half of rucksack.
        """
        self.shared_items = []
        first_half, second_half = split_list_in_half(self.rucksack)

        for item in first_half:
            if item in second_half and item not in self.shared_items:
                self.shared_items.append(item)

        self.compute_value()

    def compute_value(self):
        """Compute value of shared items based on priority.
        
        Lowercase item types a through z have priorities 1 through 26.
        Uppercase item types A through Z have priorities 27 through 52.
        """
        self.shared_items_value = 0
        for item in self.shared_items:
            self.shared_items_value += (ord(item) - 64)%32 + item.isupper()*26

    def __radd__(self, other):
        """Override summing of Elf object to sum shared items value.

        Args:
            other (Elf): Elf object to be added to the sum.

        Returns:
            Elf: Summed Elf object.
        """
        return other + self.shared_items_value

def split_list_in_half(a_list:list) -> tuple:
    """Split the list in two equally sized lists.

    Args:
        a_list (list): List to be splitted.

    Returns:
        tuple: Two parts of the splitted list.
    """
    half = len(a_list)//2
    return (a_list[:half], a_list[half:])

elves = []

if __name__ == "__main__":
    with open(os.path.join(__location__,"input.txt")) as file:
        lines = [line for line in (l.strip() for l in file)]
        for input_line in lines:       
            elf = Elf(input_line)
            elf.check_inventory()
            elves.append(elf)

print(sum(elves))