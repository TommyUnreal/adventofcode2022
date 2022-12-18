import os
from copy import deepcopy
from math import copysign
from itertools import cycle
from itertools import chain
from dataclasses import dataclass

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def move_toward_zero(n:int) -> int:
    """Move n one closer to zero by 1."""
    return n - copysign(1, n) if abs(n) > 1 else 0

def drop_stone(rock:list, high=-1)->list:
    """By default drops stone by one. Can be used to place it to certain high with optional parameter.

    Args:
        rock (list[list(int)]): Rock to be moved.
        move (int): How many indexes shall be dropped (default by 1)

    Returns:
        list: moved rock
    """
    for i in range(len(rock)):
        for j in range(len(rock[i])):
            if rock[i][j] != 0:
                rock[i][j] += high
    return rock

def move_stone(rock:list, move:int)->list:
    """Move rock by move to left or right. Negative move is to the left.

    Args:
        rock (list[list(int)]): Rock to be moved.
        move (int): How many indexes shall be moved (negative to left)

    Returns:
        list: moved rock
    """
    num_rows = len(rock)
    num_cols = len(rock[0])
    move     = int(move)
    # If the move is negative, remove "move" columns from the left and add "move" columns to the right
    if move < 0:
        new_rock = [row[-move:] + [0] * -move for row in rock]
    # If the move is positive, remove "move" columns from the right and add "move" columns to the left
    elif move > 0:
        new_rock = [[0] * move + row[:num_cols-move] for row in rock]       
    else:
        new_rock = rock

    # If the number of columns in the new list is different from the original, return the original list
    if sum(map(sum,new_rock)) != sum(map(sum,rock)):
        new_rock = move_stone(rock, move_toward_zero(move))
    
    return new_rock

def can_move_stone(stone:list, chamber:list, move:int):
    """Check if move is valid."""
    moved_stone = move_stone(stone, move)
    for row in moved_stone:
        for i in range(7):
            if row[i] != 0 and row[i] in chamber[i]:
                return False
    return True

def can_drop_stone(stone:list, chamber:list):
    """Check if drop is valid."""
    moved_stone = drop_stone(stone)
    for row in moved_stone:
        for i in range(7):
            if row[i] != 0 and row[i] in chamber[i]:
                return False
    return True


if __name__ == "__main__":
    with open(os.path.join(__location__,"input.txt")) as file:
        lines = [line for line in (l.strip() for l in file)]


        rocks = cycle([
            [[0, 0, 1, 1, 1, 1, 0]], 

            [[0, 0, 0, 1, 0, 0, 0],
             [0, 0, 2, 2, 2, 0, 0],
             [0, 0, 0, 3, 0, 0, 0]],

            [[0, 0, 1, 1, 1, 0, 0],
             [0, 0, 0, 0, 2, 0, 0],
             [0, 0, 0, 0, 3, 0, 0]],

            [[0, 0, 1, 0, 0, 0, 0],
             [0, 0, 2, 0, 0, 0, 0],
             [0, 0, 3, 0, 0, 0, 0],
             [0, 0, 4, 0, 0, 0, 0]],

            [[0, 0, 1, 1, 0, 0, 0],
             [0, 0, 2, 2, 0, 0, 0]]
        ])

        jets = cycle([*lines[0]])

        chamber  = [[1], [1], [1], [1], [1], [1], [1]] #[0, 0, 0 , 0, 0, 0, 0]
        can_move = False
        can_drop = False
        stone    = None

        for turn in range(1, 2023):
            print(f"----- Turn {turn} ----")
            #summon next stone
            stone = deepcopy(rocks.__next__())
            stone = drop_stone(deepcopy(stone), max(chain.from_iterable(chamber)) + 4)

            while can_drop_stone(deepcopy(stone), chamber):
                if str(jets.__next__()) == "<":
                    movement = -1
                    print("<")
                else:
                    movement = 1
                    print(">")
                               
                if can_drop_stone(deepcopy(stone), chamber):
                    print("Can drop!")
                    stone = deepcopy(drop_stone(stone))
                    print(stone)

                if can_move_stone(deepcopy(stone), chamber, movement):
                    print("Can move!")
                    stone = deepcopy(move_stone(stone, movement))
                    print(stone)

                if sum(map(sum,deepcopy(stone))) == 0: break            


            #safe state of chamber
            for row in stone:
                for i in range(7):
                    chamber[i].append(row[i])

        print(max(chain.from_iterable(chamber)) - 1)