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

def can_move_stone(stone:list, chamber:list, move:int)->bool:
    """Check if move is valid."""
    moved_stone = move_stone(stone, move)
    for row in moved_stone:
        for i in range(7):
            if row[i] != 0 and row[i] in chamber[i]:
                return False
    return True

def can_drop_stone(stone:list, chamber:list)->bool:
    """Check if drop is valid."""
    moved_stone = drop_stone(stone)
    for row in moved_stone:
        for i in range(7):
            if row[i] != 0 and row[i] in chamber[i]:
                return False
    return True

def get_profile(chamber:list)->list:
    """Calculate the profile of a 2D list.
    
    Do this by finding the highest element of each inner list and then subtracting the lowest
    value from each element.

    Args:
        chamber (list): A 2D list of integers.

    Returns:
        list: A list of integers containing the profile of the input list.
    """
    profile = []

    for inner_list in chamber:
        profile.append(max(inner_list))

    min_val = min(profile)

    return tuple([val - min_val for val in profile])

def has_matching_tuple_123(set_of_tuples:set, record:tuple) -> tuple:
    """Return true if elements on index 1, 2, and 3 are matching, False otherwise."""
    for t in set_of_tuples:
        if t[1] == record[1] and t[2] == record[2] and t[3] == record[3]:
            return t
    return None

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

        rocks_i    = 0
        rocks_size = 5
        jets_i     = 0
        jets_size  = len(lines[0])
        profile    = get_profile(chamber)
        hashmap    = set()
        record     = None
        record_2   = None

        turn       = 0

        while turn <= 1000000000000:
            turn += 1

            #summon next stone
            stone = deepcopy(rocks.__next__())
            stone = drop_stone(deepcopy(stone), max(chain.from_iterable(chamber)) + 4)
            rocks_i += 1

            while can_drop_stone(deepcopy(stone), chamber):
                jets_i += 1
                if str(jets.__next__()) == "<":
                    movement = -1
                    #print("<")
                else:
                    movement = 1
                    #print(">")
                               
                if can_drop_stone(deepcopy(stone), chamber):
                    #print("Can drop!")
                    stone = deepcopy(drop_stone(stone))
                    #print(stone)

                if can_move_stone(deepcopy(stone), chamber, movement):
                    #print("Can move!")
                    stone = deepcopy(move_stone(stone, movement))
                    #print(stone)

            #safe state of chamber
            for row in deepcopy(stone):
                for i in range(7):
                    chamber[i].append(row[i])

            # record (stone number, rock index,         jet index,        chamber profile,      tower height)
            record   = (turn, rocks_i%rocks_size, jets_i%jets_size, get_profile(chamber), max(chain.from_iterable(chamber)) - 1)
            record_2 = has_matching_tuple_123(hashmap, record)
            if record_2 == None:
                hashmap.add(tuple(record))
            elif record[0] > 985:
                hashmap = set()
                stones_per_cycle = record[0]-record_2[0]
                height_per_cycle = record[4]-record_2[4]
                extra_cycles     = (1000000000000-record[0])//stones_per_cycle
                

                print(record)
                print(record_2)
                print(record[0], record_2[0], stones_per_cycle, height_per_cycle, extra_cycles)

                for i in range(7):
                    chamber[i].append(max(chamber[i])+extra_cycles*height_per_cycle)

                turn += extra_cycles*stones_per_cycle
                print(turn, max(chain.from_iterable(chamber)) - 1)

        # bigger than 1528323696915
        # bigger than 1528323699395
        print(max(chain.from_iterable(chamber)) - 2)