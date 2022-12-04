import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

class ElfPair():
    """Class to hold pair of elves and sections in their responsibility."""

    def __init__(self, pair: str) -> None:
        """Transform line output and save to elf_1_sections elf_2_sections attributes.

        Section interval in "pair" input are separated with "-", elves with ",".

        Args:
            pair (str): Input line in format "2-4,6-8".
        """
        pair = pair.split(",")
        self.elf_1_sections = [int(section) for section in pair[0].split("-")]
        self.elf_2_sections = [int(section) for section in pair[1].split("-")]
    
    def sections_fully_contained(self) -> bool:
        """Compute if range of sections in pair responsibility fully contain the other.

        Returns:
            bool: True if fully contained, False otherwise.
        """
        if   self.elf_1_sections[0] <= self.elf_2_sections[0] and self.elf_1_sections[1] >= self.elf_2_sections[1]:
            return True
        elif self.elf_1_sections[0] >= self.elf_2_sections[0] and self.elf_1_sections[1] <= self.elf_2_sections[1]:
            return True
        else:
            return False

if __name__ == "__main__":
    with open(os.path.join(__location__,"input.txt")) as file:
        lines = [line for line in (l.strip() for l in file)]
        a_sum = 0

        for line in lines:
            elf_pair = ElfPair(line)
            
            if elf_pair.sections_fully_contained():
                a_sum += 1

        print(a_sum)