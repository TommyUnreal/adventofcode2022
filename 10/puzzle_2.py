import os
from dataclasses import dataclass

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

@dataclass
class Instruction():
    cycle: int = 0
    add: int = 0

    def __lt__(self, other):
        return self.cycle < other.cycle

if __name__ == "__main__":
    with open(os.path.join(__location__,"input.txt")) as file:
        lines = [line for line in (l.strip() for l in file)]

        register = 1
        a_sum = 0
        operations = []
        cycle = 1

        for i, line in enumerate(lines):
            if "noop" in line:
                cycle += 1
                operations.append(Instruction(cycle, 0))
            if "addx " in line:
                cycle += 2
                operations.append(Instruction(cycle, int(line.split(" ")[1])))

        crt = [["." for i in range(40)] for j in range(6)]
        

        row = 0
        for cycle in range(1,241): 

            for i in sorted(operations):
                if cycle == i.cycle:
                    register += i.add

            if (register) == (cycle%40) or \
                (register+1) == (cycle%40) or \
                (register+2) == (cycle%40):
                crt[row][cycle%40-1] = "#"

            if cycle in [40, 80, 120, 160, 200]:
                row += 1

        print('\n'.join([''.join([str(cell) for cell in row]) for row in crt]))