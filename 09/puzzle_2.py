import os
from dataclasses import dataclass
import numpy as np

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

@dataclass
class Coordinates():
    """Dataclass to hold information about x and y position."""
    x: int = 0
    y: int = 0

def get_tail_pos(head_pos, tail_pos):
    """Compute position of knot lagging behind.
    
    If the head is ever two steps directly up, down, left, or right from the tail, 
    the tail must also move one step in that direction. Otherwise, if the head 
    and tail aren't touching and aren't in the same row or column, the tail always 
    moves one step diagonally to keep up.

    Args:
        head_pos (Coordinates): Position of leading knot after it moves.
        tail_pos (Coordinates): Position of lagging knot before it moves.

    Returns:
        Coordinates: Return updated position of the lagging rope tail.
    """
    if abs(head_pos.x - tail_pos.x) > 1 or abs(head_pos.y - tail_pos.y) > 1:
        shift = Coordinates()
        if abs(head_pos.x - tail_pos.x) == 2 and abs(head_pos.y - tail_pos.y) == 1:
            shift.y = head_pos.y - tail_pos.y
        if abs(head_pos.x - tail_pos.x) == 1 and abs(head_pos.y - tail_pos.y) == 2:
            shift.x = head_pos.x - tail_pos.x
        tail_pos.x = ((head_pos.x + tail_pos.x - shift.x) / 2) + shift.x
        tail_pos.y = ((head_pos.y + tail_pos.y - shift.y) / 2) + shift.y
    return tail_pos

if __name__ == "__main__":
    with open(os.path.join(__location__,"input.txt")) as file:
        lines = [line.split(" ") for line in (l.strip() for l in file)]
        trees_l = []

        all_t_pos = []
        knot_pos  = []
        for i in range(10):
            knot_pos.append(Coordinates())
            all_t_pos.append(set())
            all_t_pos[i].add((knot_pos[i].x, knot_pos[i].y))

        for line in lines:
            direction = line[0]
            steps     = int(line[1])

            for step in range(steps):
                if direction == "U":
                    knot_pos[0].y += 1
                elif direction == "D":
                    knot_pos[0].y -= 1
                elif direction == "R":
                    knot_pos[0].x += 1
                else: #direction == "L":
                    knot_pos[0].x -= 1
                for i in range(0, 9):
                    knot_pos[i+1] = get_tail_pos(knot_pos[i], knot_pos[i+1])
                    all_t_pos[i+1].add((knot_pos[i+1].x, knot_pos[i+1].y))
        
        print(all_t_pos[9])
        print(len(all_t_pos[9]))

