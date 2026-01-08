import sys
import curses
import time
from errors import ParseError
from MazeGenerator import MazeGenerator

class Canvas:
    def __init__(self):
        self.screen = curses.initscr()

    def render(self):
        window = curses.newwin(16, 16, 8, 8)
        window.addstr(8, 8, "A")
        window.refresh()
        window.getch()

if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise ParseError("Bad Parameters")
        maze = MazeGenerator((16, 16), 1)
        maze.solve('algorithm')
        canvas = Canvas()
        canvas.render()
    except ParseError as error:
        sys.stderr.write(str(error))
        sys.stderr.flush()
