import os
import numpy as np
from dataclasses import dataclass
from collections import deque

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

@dataclass
class Point():
    """Dataclass to hold information about x and y position."""
    x: int = 0
    y: int = 0
 
# A data structure for queue used in BFS
class queueNode:
    def __init__(self,pt: Point, dist: int):
        self.pt = pt  # The coordinates of the cell
        self.dist = dist  # Cell's distance from the source
 
# Check whether given cell(row,col)
# is a valid cell or not
def isValid(row: int, col: int):
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)
 
# These arrays are used to get row and column
# numbers of 4 neighbours of a given cell
rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]

def BFS(mat, src: Point, dest: Point):
    # check source and destination cell
    # of the matrix have value 1
    #if abs(mat[src.x][src.y] - mat[dest.x][dest.y]) > 1:
    #    return -1

    visited = [[False for i in range(COL)]
                       for j in range(ROW)]
     
    # Mark the source cell as visited
    visited[src.x][src.y] = True
    # Create a queue for BFS
    q = deque()
    # Distance of source cell is 0
    s = queueNode(src,0)
    q.append(s) #  Enqueue source cell
     
    # Do a BFS starting from source cell
    while q:
 
        curr = q.popleft() # Dequeue the front cell
         
        # If we have reached the destination cell,
        # we are done
        pt = curr.pt
        if pt.x == dest.x and pt.y == dest.y:
            return curr.dist
         
        # Otherwise enqueue its adjacent cells
        for i in range(4):
            row = pt.x + rowNum[i]
            col = pt.y + colNum[i]
             
            # if adjacent cell is valid, has path 
            # and not visited yet, enqueue it.
            if (isValid(row,col) and
               (mat[row][col] - mat[pt.x][pt.y]) <= 1 and
                not visited[row][col]):
                visited[row][col] = True
                Adjcell = queueNode(Point(row,col),
                                    curr.dist+1)
                q.append(Adjcell)
     
    # Return -1 if destination cannot be reached
    return -1

if __name__ == "__main__":
    with open(os.path.join(__location__,"input.txt")) as file:
        lines = [line for line in (l.strip() for l in file)]

        input_array = []
        start = Point()
        finish = Point()

        for y, line in enumerate(lines):
            temp = [] 
            for x, char in enumerate(line):
                if char == "S": #a
                    temp.append(0)
                    start.x, start.y = y, x
                elif char == "E": #z
                    temp.append(26)
                    finish.x, finish.y = y, x
                else:
                    temp.append((ord(char) - 64)%32 + char.isupper()*26)
            input_array.append(temp)

    the_map = np.array(input_array)
    ROW, COL = the_map.shape
    shortest = 9999

    for y in range(ROW):
        for x in range(COL):
            if the_map[y][x] <= 1:
                start.x, start.y = y, x
                dist = BFS(the_map.tolist(),start,finish)
                print(dist)
                if dist != -1 and dist < shortest:
                    shortest = dist
    
    
    print(the_map)

    print("Shortest Path is",shortest)



