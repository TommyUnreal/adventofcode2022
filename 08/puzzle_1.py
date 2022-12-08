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
        self.highest = numpy.zeros_like(trees)

    def direction_check(self):
        """Compute what trees are visible and print how many.
        
        TODO:
            Repeating code could be avoided with method independent on direction.
        """
        for i, row in enumerate(self.trees):
            visible = -1
            for j in range(len(row)):
                if self.trees[i][j] > visible:
                    visible = self.trees[i][j]
                    self.highest[i][j] = 1

            visible = -1        
            for j in range(len(row)):
                if numpy.flip(self.trees)[i][j] > visible:
                    visible = numpy.flip(self.trees)[i][j]
                    numpy.flip(self.highest)[i][j] = 1
                
        for i, col in enumerate(self.trees.T):
            visible = -1
            for j in range(len(col)):
                if self.trees.T[i][j] > visible:
                    visible = self.trees.T[i][j]
                    self.highest.T[i][j] = 1

            visible = -1        
            for j in range(len(col)):
                if numpy.flip(self.trees.T)[i][j] > visible:
                    visible = numpy.flip(self.trees.T)[i][j]
                    numpy.flip(self.highest.T)[i][j] = 1

            print(f"{self.highest} \n\n Number of visible trees: {sum(sum(self.highest))}")

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
        grove.direction_check()



