import sys
from utils.ErrorHandler import ParseError
from utils.MazeGenerator import MazeGenerator
from utils.Display import Curses

if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise ParseError("Bad Parameters")
    except ParseError as error:
        sys.stderr.write(str(error))
        sys.stderr.flush()
        sys.exit(1)
    maze = MazeGenerator((8, 8), 1)
    maze.generate()
    maze.print()
    canvas = Curses()
    canvas.display(maze.matrix)
