import os
import numpy as np

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def store_voxels(lines:list[str])->np.ndarray:
    """Store voxels in a 3D numpy array.

    Args:
        lines (list[str]): List of strings representing voxel coordinates in the form "x,y,z".

    Returns:
        numpy.ndarray: 3D numpy array with 1s at the coordinates specified in the `lines` list and 0s at all other coordinates.
    """
    max_x, max_y, max_z = 0, 0, 0
    for line in lines:
        x, y, z = map(int, line.split(','))
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        max_z = max(max_z, z)
    shape = (max_x + 1, max_y + 1, max_z + 1)
    voxels = np.zeros(shape, dtype=int)
    for line in lines:
        x, y, z = map(int, line.split(','))
        voxels[x, y, z] = 1
    return voxels

def calculate_surface_area(voxels):
    """
    Calculate the surface area of a 3D object represented by a 3D numpy array of 1s and 0s.

    Args:
        voxels (numpy.ndarray): 3D numpy array with 1s representing the voxels of the object and 0s representing the empty space.

    Returns:
        int: The surface area of the object.
    """
    # Create a 3D numpy array of zeros with the same shape as the input array
    surface = np.zeros_like(voxels)

    # Iterate through the voxels and check if each voxel has at least one neighboring voxel with value 0
    for i in range(voxels.shape[0]):
        for j in range(voxels.shape[1]):
            for k in range(voxels.shape[2]):
                if voxels[i, j, k] == 1:
                    # Initialize the surface area of the voxel to 6
                    surface_area = 6
                    # Check the 6 neighboring voxels
                    if i > 0 and voxels[i - 1, j, k] == 1:
                        surface_area -= 1
                    if i < voxels.shape[0] - 1 and voxels[i + 1, j, k] == 1:
                        surface_area -= 1
                    if j > 0 and voxels[i, j - 1, k] == 1:
                        surface_area -= 1
                    if j < voxels.shape[1] - 1 and voxels[i, j + 1, k] == 1:
                        surface_area -= 1
                    if k > 0 and voxels[i, j, k - 1] == 1:
                        surface_area -= 1
                    if k < voxels.shape[2] - 1 and voxels[i, j, k + 1] == 1:
                        surface_area -= 1
                    # Add the surface area of the voxel to the surface array
                    surface[i, j, k] = surface_area

    # Sum the values in the surface array to get the total surface area
    total_surface_area = surface.sum()

    return total_surface_area


if __name__ == "__main__":

    with open(os.path.join(__location__,"input.txt")) as file:
        lines = [line for line in (l.strip() for l in file)]
        
        voxels = store_voxels(lines)

    np.set_printoptions(threshold=np.inf)
    print(calculate_surface_area(voxels))