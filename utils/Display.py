import curses
from utils.CellController import CellController

class Curses:
    def __init__(self):
        self.screen = curses.initscr()

    @staticmethod
    def _cell_to_ansi(cell):
        # 1111 => east north west south => 8 4 2 1
        if cell['east']:
            return "E"
        if cell['north']:
            return "N"
        if cell['west']:
            return "W"
        if cell['south']:
            return "S"
        return "0"

    def display(self, matrix):
        base = "0123456789ABCDEF"
        h, w = self.screen.getmaxyx()
        rows = len(matrix)
        cols = len(matrix[0])
        print(f"Height: {h}/{rows}/{int((h - rows) / 2)}, Width: {w}/{cols}/{int((w - cols) / 2)}")
        window = curses.newwin((rows * 2) + 1, (cols * 2) + 1, int((h - (rows * 2)) / 2), int((w - (cols * 2)) / 2))
        for row in range(rows):
            for col in range(cols):
                cell = CellController(matrix[row][col])
                raw_cell = matrix[row][col]
                y = ((row) * 2) + 1
                x = ((col) * 2) + 1
                if raw_cell['north']:
                    window.addch(y - 1, x, '█')
                if raw_cell['north'] or raw_cell['west']:
                    window.addch(y - 1, x - 1,'█')
                if raw_cell['west']:
                    window.addch(y, x + 1, '█')
                if raw_cell['west'] or raw_cell['south']:
                    window.addch(y - 1, x + 1, '█')
                if raw_cell['south']:
                    window.addch(y + 1, x, '█')
                if raw_cell['south'] or raw_cell['east']:
                    window.addch(y + 1, x + 1, '█')
                if raw_cell['east']:
                    window.addch(y, x - 1, '█')
                if raw_cell['east'] or raw_cell['north']:
                    window.addch(y + 1, x - 1, '█')
                # window.addch(y, x, cell.hexadecimal())
                # window.addstr(row, col, self._cell_to_ansi(cell.raw()))
        window.refresh()
        window.getch()
