import os
from dataclasses import dataclass

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

class Dir():
    """Dataclass for holding information about directories.
    
    Attr:
        parent(Dir): Object representing hierarchically superior directory.
        name(str): Name of the directory.
        dirs(list): List of object representing to hierarchically inferior directories.
        files(list): List of object representing  files in the directory.
    """

    def __init__(self, name:str, parent=None):
        """Basic constructor."""
        self.parent = parent
        self.name = name
        self.dirs = []
        self.files = []

    def get_size(self) -> int:
        """Compute directory size including child directories (recursively).

        Returns:
            int: Return directory size including child directories.
        """
        retval = 0

        for f in self.files:
            retval += f.size

        for d in self.dirs:
            retval += d.get_size()

        return retval

    def add_dir(self, dir):
        """Add new directory to dirs list.

        Args:
            dir (Dir): Dir object to be added as child.
        """
        self.dirs.append(dir)

    def add_file(self, file):
        """Add new file to files list.

        Args:
            dir (File): File object to be added as directory content.
        """
        self.files.append(file)

    def print_disc(self, indentation):
        """Recursively pretty print whole dir and file structure.

        Args:
            indentation (str): Indentation for recursive call.
        """
        print(f"{indentation}{self.name} {self.get_size()}")
        indentation += " "
        global sizes
        sizes.append(self.get_size())
        for f in self.files:
            f.print_file(indentation)
        for d in self.dirs:
            d.print_disc(indentation)
        

@dataclass
class File():
    """Dataclass for holding information about files.
    
    Attr:
        size(int): File size in bytes.
        name(str): Name of the file.
    """
sizes = []

if __name__ == "__main__":
    with open(os.path.join(__location__,"input.txt")) as file:
        lines = [line for line in (l.strip() for l in file)]

        root = Dir("\\")
        pointer = root

        for line in lines:
            #print(line)
            if "$ cd /" in line:
                pointer = root
                #print("Going to the root \\")
            elif "$ cd .." in line:
                pointer = pointer.parent
                #print(f"Going to the the parent {pointer.name}")
            elif "$ cd " in line:
                #print(f"Adding dir {line.split(' ')[2]} to {pointer.name}")
                new_dir = Dir(line.split(" ")[2], parent=pointer)
                pointer.add_dir(new_dir)
                pointer = new_dir
            elif line == "$ ls":
                #print(f"ls command")
                pass
            else:
                if "dir" not in line:
                    ls_result = line.split(" ")
                    #print(f"Adding file {ls_result[1]} of size {int(ls_result[0])}")
                    pointer.add_file(File(int(ls_result[0]), ls_result[1]))
        
        root.print_disc("")
        free_space = 70_000_000 - root.get_size()
        big_enough = [size for size in sizes if (size + free_space) > 30_000_000]
        print(min(big_enough))