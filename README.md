### Advent of Code 2022
This repository contains solution of https://adventofcode.com/2022.

Puzzles in folders with **`_by_ai`** suffix were solved using [Large Language Model](https://techcrunch.com/2022/04/28/the-emerging-types-of-language-models-and-why-they-matter/) [bloom](https://huggingface.co/bigscience/bloom). **This means that a working code was generated by another code, not human by programmer!** I just transformed Puzzle to simpler form. The input for LLM is documented in every generated py-file.

### Thanks
Great thanks goes to to [Eric Wastl](https://twitter.com/ericwastl) for Puzzles!

### Highlights & Lesson learned
#### Day 1
**`HIHGLIGHT`** Searching max 3 translates to $O(3n)$, sorting the list to $O(n \log n)$. And I like it.

**`LESSON`** I have entered AoC via google autentification. Keep that in mind. 🤣

#### Day 2
**`HIHGLIGHT`** Fancy terminal output be like:
```
🧝 plays ✌️, 👱 play ✌️! Game score is 6.
🧝 plays ✋, 👱 play ✋! Game score is 5.
🧝 plays ✊, 👱 play ✋! Game score is 8.
🧝 plays ✊, 👱 play ✊! Game score is 4.
🧝 plays ✋, 👱 play ✋! Game score is 5.
```

**`LESSON`** To override sum function, use
```python
    def __radd__(self, other):
        return other + self.score
```

#### Day 3
**`HIHGLIGHT`** With the second day in three days dealing with an inventory of elves, we are heading into RPG territory.
```python
class Elf():
    """Class for keeping track of elf and it's in inventory."""
```

**`LESSON`** To group content of a list (or other iterable) using itertools:
```python
def group_list(n, iterable:list) -> list:
    """Group iterable to list of tuples of size n."""
    args = [iter(iterable)] * n
    return list(zip_longest(*args))
```

**`LESSON`** To find intersection of multiple lists very fast:
```python
def find_intersection(list_of_lists:list) -> list:
    """Find the intersection of all lists in list_of_lists."""
    return list(set.intersection(*[set(list) for list in list_of_lists]))
```

#### Day 4
**`HIHGLIGHT`** Writing (as much as I can) maintainable code takes me about 3x more time. Usually, it pays back a little in the second puzzle. This time adding one extra method did it. And I used the lesson from yesterday, yay!
```python
def sections_intersect(self) -> bool:
    """Compute if range of sections in pair responsibility intersect the other.

    Returns:
        bool: True if ranges intersect, False otherwise.
    """
    return bool(find_intersection([
        range(self.elf_1_sections[0], self.elf_1_sections[1]+1), 
        range(self.elf_2_sections[0], self.elf_2_sections[1]+1)
        ]))
```

**`LESSON`** *Readability counts.* This is the 7th line of [Zen of Python](https://peps.python.org/pep-0020/). The older I'm the more I understand this 🤣. That's why I decided to document the code well this year.
```python
def __init__(self, pair: str) -> None:
    """Transform line output and save to elf_1_sections elf_2_sections attributes.

    Section interval in "pair" input are separated with "-", elves with ",".
    
    Args:
        pair (str): Input line in format "2-4,6-8".
    """
    pair = pair.split(",")
    self.elf_1_sections = [int(section) for section in pair[0].split("-")]
    self.elf_2_sections = [int(section) for section in pair[1].split("-")]
```

#### Day 5
**`HIHGLIGHT`** I really liked the twist, that in the second puzzle the crane could lift multiple crates. But here writing an object-oriented solution was maybe elegant, but took me over 40 minutes to write for both parts together!

**`LESSON`** To define the default empty list in the data class you have to actually import `field` from `dataclasses` like this:
```python
from dataclasses import dataclass, field

@dataclass
class Stack():
    content: list = field(default_factory=list)
```

**`LESSON`** To parse all numbers in str into a list of integers, you can do a simple oneliner:
```python
import re

list_of_numbers_from_str = [int(n) for n in re.findall(r'\d+',line)]
```

**`LESSON`** If time is an issue, it might be faster to edit the input manually. I reminded myself of the 8th line of [Zen of Python](https://peps.python.org/pep-0020/) this time: Special cases aren't special enough to break the rules. Parsing it and writing methods to load the state of it into objects saved me 10-15 minutes. I wrote those later on Day 6.
```
[C]         [S] [H]                
[F] [B]     [C] [S]     [W]        
[B] [W]     [W] [M] [S] [B]        
[L] [H] [G] [L] [P] [F] [Q]        
[D] [P] [J] [F] [T] [G] [M] [T]    
[P] [G] [B] [N] [L] [W] [P] [W] [R]
[Z] [V] [W] [J] [J] [C] [T] [S] [C]
[S] [N] [F] [G] [W] [B] [H] [F] [N]
 1   2   3   4   5   6   7   8   9 
```

#### Day 6
**`HIHGLIGHT`** So far easiest puzzle to program. No objects this time!

**`LESSON`** Oneliner to check if objects in an iterable do not repeat:
```python
if len(list) == len(set(list)):
    print("Objects do not repeat!")
```

#### Day 7
**`HIHGLIGHT`** Recursion in action! It can create such a elegant solutions. Like this structured output in 6 lines of code!
```python
\ 48381165
 -b.txt 14848514
 -c.dat 8504156
 a 94853
  -f 29116
  -g 2557
  -h.lst 62596
  e 584
   -i 584
...
```
```python
print(f"{indentation}{self.name} {self.get_size()}")
indentation += " "
for f in self.files:
    f.print_file(indentation)
for d in self.dirs:
    d.print_disc(indentation)
```
**`LESSON`** If you get a change request, issue, puzzle, or any task really... **Read the specification carefully!** You will then not spend 15 minutes answering a question nobody asked.


#### Day 8
**`HIHGLIGHT`** It was great to refresh numpy. I believe this wasn't the last time in this year's AoC, just a sneak peek for the things to come.

**`LESSON`** You dont need complicate your life when thinking about indexes, if you need to make operations in up/down/left/right directions. NUpy is here to save you. Just prepare your algortihm for one side, than use:
```python
import numpy as np

2d_array = np.array(2d_list)

do_your_code(2d_array)            # original direction
do_your_code(np.flip(2d_array))   # opposite direction same axis
do_your_code(2d_array.T)          # original direction 2nd axis
do_your_code(np.flip(2d_array.T)) # opposite direction 2nd axis
```

**`LESSON`** Apparently for cycle have else case, which is executed, when the cycle finished without interrupts (f.e.  `break`). This is awrsome when you need it. How come I have never heard about it?
```python
for index in range(5):
    if index > 3: break
else:
    print("This is not executed.")

for index in range(5):
    if index > 10: break
else:
    print("This is executed.")
```
