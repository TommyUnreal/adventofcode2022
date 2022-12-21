import os
import re
from collections import deque

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def eval_monkey(monkey, lines):
    """Recursively use python eval to solve monkey equation."""
    if re.findall(r'\d+',lines[monkey]):
        return int(lines[monkey])

    monkey_1, operand, monkey_2 = lines[monkey].split()
    lines[monkey] = eval(f"eval_monkey('{monkey_1}', lines) {operand} eval_monkey('{monkey_2}', lines)")
    
    return lines[monkey]

if __name__ == "__main__":
    with open(os.path.join(__location__,"input.txt")) as file:
        lines = {line.split(":")[0]:line.split(":")[1] for line in (l.strip() for l in file)}
        print(eval_monkey("root", lines))