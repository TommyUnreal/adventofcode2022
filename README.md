### Advent of Code 2022
Solution of https://adventofcode.com/2022

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
