import os
import re
from dataclasses import dataclass, field
import sys

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

@dataclass
class Monkey():
    number: int = 0
    held_items: list = field(default_factory=list)
    inspected: int = 0
    operation_type: str = "plus"
    operation_num: int = 0
    test: int = 0
    if_true: int = 0
    if_false: int = 0

    def inspect_item(self) -> tuple:
        if not self.held_items:
            return (-1, -1)
        else:
            self.inspected += 1
            worry_level = self.held_items.pop(0)

            print(f"  Monkey inspects an item with a worry level of {worry_level}.")

            match self.operation_type:
                case "plus":
                    worry_level += self.operation_num
                    print(f"    Worry level increases by {self.operation_num} to {worry_level}.")
                case "mul":
                    worry_level *= self.operation_num
                    print(f"    Worry level multiplied by {self.operation_num} to {worry_level}.")
                case "pow":
                    worry_level *= worry_level
                    print(f"    Worry level multiplied by itself to {worry_level}.")
            worry_level = worry_level // 3

            if worry_level % self.test == 0:
                print(f"    Current worry level is divisible by {self.test}.")
                print(f"    Item with worry level {worry_level} is thrown to monkey {self.if_true}.")
                return (worry_level, self.if_true)
            else:
                print(f"    Current worry level is NOT divisible by {self.test}.")
                print(f"    Item with worry level {worry_level} is thrown to monkey {self.if_false}.")
                return (worry_level, self.if_false)

    def __lt__(self, other):
        """Overload < operator for comparing monkeys."""
        return self.inspected < other.inspected

    def __str__(self) -> str:
        return f"inspected: {self.inspected}, test: {self.test},  items: {self.held_items}, true - {self.if_true}, false - {self.if_false}"

if __name__ == "__main__":
    with open(os.path.join(__location__,"input.txt")) as file:
        lines = [line for line in (l.strip() for l in file)]

        monkeys = []

        number = 0
        held_items = []
        inspected = 0
        operation_type = "plus"
        operation_num = 0
        test = 0
        if_true = 0
        if_false = 0


        for line in lines:
            if "Monkey " in line:
                number = [int(n) for n in re.findall(r'\d+',line)][0]
            elif "Starting items: " in line:
                held_items = [int(n) for n in re.findall(r'\d+',line)]
            elif "Operation: " in line:
                if "new = old +" in line:
                    operation_type = "plus"
                    operation_num = [int(n) for n in re.findall(r'\d+',line)][0]
                elif "new = old * old" in line:
                    operation_type = "pow"
                    operation_num = 0
                else:
                    operation_type = "mul"
                    operation_num = [int(n) for n in re.findall(r'\d+',line)][0]
            elif "Test: divisible by " in line:
                test = [int(n) for n in re.findall(r'\d+',line)][0]
            elif "If true: throw to monkey" in line:
                if_true = [int(n) for n in re.findall(r'\d+',line)][0]
            elif "If false: throw to monkey" in line:
                if_false = [int(n) for n in re.findall(r'\d+',line)][0]
            else:
                if held_items:
                    monkeys.append(Monkey(number, held_items, inspected, operation_type, operation_num, test, if_true, if_false))
                    held_items = []
                    inspected = 0
                    operation_type = "plus"
                    operation_num = 0
                    test = 0
                    if_true = 0
                    if_false = 0

        monkeys.append(Monkey(number, held_items, inspected, operation_type, operation_num, test, if_true, if_false))

        for monkey in monkeys:
            print(monkey)

        for i in range(20):
            print(f"Turn {i}:")
            for monkey in monkeys:
                for i in range(len(monkey.held_items)):
                    item, target = monkey.inspect_item()
                    monkeys[target].held_items.append(item)
        
        for monkey in sorted(monkeys):
            print(monkey)