import random
from utils.CellController import CellController

class MazeGenerator:
    matrix = []
    def __init__(self, size, seed):
        self.width, self.height = size
        self.seed = seed
    
    def _42(self, width, height):
        cell = CellController({ 'east': 1, 'north': 1, 'west': 1, 'south': 1 })
        self.matrix[width + 0][height + 0] = cell.raw()
        self.matrix[width + 1][height + 0] = cell.raw()
        self.matrix[width + 2][height + 0] = cell.raw()
        self.matrix[width + 2][height + 1] = cell.raw()
        self.matrix[width + 2][height + 2] = cell.raw()
        self.matrix[width + 3][height + 2] = cell.raw()
        self.matrix[width + 4][height + 2] = cell.raw()
        self.matrix[width + 0][height + 4] = cell.raw()
        self.matrix[width + 0][height + 5] = cell.raw()
        self.matrix[width + 0][height + 6] = cell.raw()
        self.matrix[width + 1][height + 6] = cell.raw()
        self.matrix[width + 2][height + 6] = cell.raw()
        self.matrix[width + 2][height + 5] = cell.raw()
        self.matrix[width + 2][height + 4] = cell.raw()
        self.matrix[width + 3][height + 4] = cell.raw()
        self.matrix[width + 4][height + 4] = cell.raw()
        self.matrix[width + 4][height + 5] = cell.raw()
        self.matrix[width + 4][height + 6] = cell.raw()

    def generate(self):
        for y in range(self.height):
            row = []
            for x in range(self.width):
                cell = CellController()
                cell.generate(random.randint(0, 9999))
                row.append(cell.raw())
            self.matrix.append(row)
        self._42(int((self.height - 5) / 2), int((self.width - 7) / 2))

    def solve(self):
        pass

    def save(self):
        pass

    def print(self):
        for line in self.matrix:
            for v in line:
                cell = CellController(v)
                # print((v))
                print(cell.hexadecimal(), end="")
            print("")
        pass
