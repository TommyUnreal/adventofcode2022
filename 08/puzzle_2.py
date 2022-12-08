import os
import numpy

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

class Grove():
    """Wrapper class for peculiar patch of tall trees."""


    def __init__(self, trees: int):
        """Constructor for Grove, keeps tree info in numpy.array.

        Args:
            trees (int): 2D List of int values describing tree grind and tree sizes. 
        """
        self.trees = numpy.array(trees)
        self.scenic_score = numpy.ones_like(trees)

    def find_house_location(self):
        """Find and print best location based on scenic view.
        
        To measure the viewing distance from a given tree, look up, down, left, and right from that tree;
        stop if you reach an edge or at the first tree that is the same height or taller than the tree under 
        consideration. (If a tree is right on the edge, at least one of its viewing distances will be zero.)

        TODO:
            Repeating code could be avoided with method independent on direction.
        """
        for x in range(self.trees.shape[1]):
            for y in range(self.trees.shape[0]):
                i = 0
                for i in range(1,y+1,1):
                    if self.trees[x][y-i] >= self.trees[x][y]:
                        self.scenic_score[x][y] = self.scenic_score[x][y] * i
                        #print(f"score:{i} -> {self.trees[x][y-i]}[{x},{y-i}] blocks {self.trees[x][y]}[{x},{y}]")
                        break
                else:
                    self.scenic_score[x][y] = self.scenic_score[x][y] * i
                    #print(f"[{x},{y}]:{i} -> No blocks to {self.trees[x][y]}")

        for x in range(self.trees.shape[1]):
            for y in range(self.trees.shape[0]):
                i = 0
                for i in range(1,y+1,1):
                    if numpy.flip(self.trees)[x][y-i] >= numpy.flip(self.trees)[x][y]:
                        numpy.flip(self.scenic_score)[x][y] = numpy.flip(self.scenic_score)[x][y] * i
                        break
                else:
                    numpy.flip(self.scenic_score)[x][y] = numpy.flip(self.scenic_score)[x][y] * i

        for x in range(self.trees.T.shape[1]):
            for y in range(self.trees.T.shape[0]):
                i = 0
                for i in range(1,y+1,1):
                    if self.trees.T[x][y-i] >= self.trees.T[x][y]:
                        self.scenic_score.T[x][y] = self.scenic_score.T[x][y] * i
                        break
                else:
                    self.scenic_score.T[x][y] = self.scenic_score.T[x][y] * i

        for x in range(self.trees.T.shape[1]):
            for y in range(self.trees.T.shape[0]):
                i = 0
                for i in range(1,y+1,1):
                    if numpy.flip(self.trees.T)[x][y-i] >= numpy.flip(self.trees.T)[x][y]:
                        numpy.flip(self.scenic_score.T)[x][y] = numpy.flip(self.scenic_score.T)[x][y] * i
                        break
                else:
                    numpy.flip(self.scenic_score.T)[x][y] = numpy.flip(self.scenic_score.T)[x][y] * i

        print(f"{self.scenic_score} \n\nHighest scenic score: {max(map(max, self.scenic_score))}")

if __name__ == "__main__":
    with open(os.path.join(__location__,"input.txt")) as file:
        lines = [line for line in (l.strip() for l in file)]
        trees_l = []

        for line in lines:
            temp = []
            for i in range(len(line)):
                temp.append(int(line[i]))
            trees_l.append(temp)

        grove = Grove(trees_l)
        grove.find_house_location()

