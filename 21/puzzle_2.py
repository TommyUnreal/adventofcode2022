import os
import re
from copy import deepcopy
from collections import deque

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def eval_monkey(monkey, lst):
    """Recursively use python eval to solve monkey equation."""
    monkeys = deepcopy(lst)
    if type(monkeys[monkey]) == bool:
        return monkeys[monkey]
    elif re.findall(r'\d+',str(monkeys[monkey])):
            return int(monkeys[monkey])
    
    monkey_1, operand, monkey_2 = monkeys[monkey].split()
    monkeys[monkey] = eval(f"eval_monkey('{monkey_1}', monkeys) {operand} eval_monkey('{monkey_2}', monkeys)")
    
    return monkeys[monkey]

if __name__ == "__main__":
    with open(os.path.join(__location__,"input.txt")) as file:
        lines = {line.split(":")[0]:line.split(":")[1] for line in (l.strip() for l in file)}
        lines["root"] = lines["root"].replace("+", "==")

        side_a, _, side_b = lines["root"].split()

        lines["humn"]  = " 0"
        n_step         = eval_monkey(side_a, lines)
        lines["humn"]  = " 10000000000000"
        n1_step        = eval_monkey(side_a, lines)
        value_to_reach = eval_monkey(side_b, lines)

        step_gradient  = (n_step - n1_step) / 10000000000000.0
        steps_needed   = (n_step-value_to_reach) / step_gradient

        lines["humn"] = f" {int(steps_needed)}"
        print(f" left side = {eval_monkey(side_a, lines)}")
        print(f"right side = {eval_monkey(side_b, lines)}")
        print(f"{int(steps_needed)} is {eval_monkey('root', lines)}")
