import random
from typing import Optional

class CellController:
    _cell = {}
    def __init__(self, cell = None):
        self._cell = cell

    def generate(self, seed = -1):
        number = random.randint(0, 16)
        self._cell = {
            'east': 0,
            'north': 0,
            'west': 0,
            'south': 0,
        }

    def raw(self):
        return self._cell

    def hexadecimal(self):
        base = "0123456789ABCDEF"
        value = 0
        if self._cell['east']:
            value = value + 8
        if self._cell['north']:
            value = value + 4
        if self._cell['west']:
            value = value + 2
        if self._cell['south']:
            value = value + 1
        return base[value]
