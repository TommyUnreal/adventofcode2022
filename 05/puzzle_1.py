import os
import re
from dataclasses import dataclass, field

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


class Crane():
    def __init__(self, stacks: int) -> None:
        """Initialize Crane object with stacks.

        Args:
            stacks (int): Number of stacks to be initialized.
        """
        self.stacks = [Stack() for i in range(stacks)]

    def load_stacks(self, crates:list) -> None:
        """Load crates on stacks during load phase.

        Args:
            crates (list): List of crates to be loaded in same order as stacks.
        """
        if not self.stacks:
            return
        else:
            for i, crate in enumerate(crates):
                self.stacks[i].load_crate(crate)

    def move_crate(self, instructions: list) -> None:
        """Move crate from one stack to another regarding the instruction list.

        Args:
            instructions (list): list of stings in following format 
                [how many crate, from index, to index]
                Example [1, 3, 2] 1 crate from stack 4 to stack 3
        """
        if not self.stacks:
            return
        else:
            for i in range(instructions[0]):
                moved_crate = self.stacks[instructions[1]-1].pop()
                self.stacks[instructions[2]-1].add_crate(moved_crate)
                print(f"Moved crate '{moved_crate}' from {instructions[1]} to {instructions[2]}")

    def __str__(self) -> str:
        """_summary_

        Returns:
            str: String to be printed.
        """
        retval = ""
        for stack in self.stacks:
            retval += stack.get_top_crate()
        return retval

@dataclass
class Stack():
    """Dataclass to hold info about content of stacks."""
    content: list = field(default_factory=list)

    def load_crate(self, crate: str()) -> None:
        """Load a crate to stack during load phase. This is in reverse order to add_crate().

        Args:
            crate (str): Crate to be loaded.
        """
        if "-" not in crate:
            self.content.append(crate)

    def add_crate(self, crate: str()) -> None:
        """Load a crate to stack during move phase. This is in reverse order to load_crate().

        Args:
            crate (str): Crate to be loaded.
        """
        if "-" not in crate:
            self.content.insert(0, crate)
    
    def pop(self) -> str:
        """Remove and return last crate on top of the stack.

        Returns:
            str: Crate lifted.
        """
        return self.content.pop(0)

    def get_top_crate(self) -> str:
        """Return label of crate on top of the stack."""
        return self.content[0][1]

if __name__ == "__main__":
    with open(os.path.join(__location__,"input.txt")) as file:
        lines = [line for line in file]
        crane = None
        loads = []

        for line in lines:
            if "move" in line:
                #move instructions
                crane.move_crate([int(n) for n in re.findall(r'\d+',line)])
            elif "1" in line:
                crane = Crane(max([int(n) for n in re.findall(r'\d+',line)]))
                #start load phase
                for load in loads:
                    crane.load_stacks(load)
            else:
                #move phase
                line_input = re.sub("    ", " [-] ", line)
                line_input = re.sub("\n", "", line_input)
                print([c for c in line_input.split(" ") if c])
                loads.append([c for c in line_input.split(" ") if c])

        print(crane)
