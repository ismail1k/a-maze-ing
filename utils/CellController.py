import random
from typing import Optional

class CellController:
    _cell = {}
    def __init__(self, cell = None):
        self._cell = cell

    def generate(self, seed = -1):
        number = random.randint(0, 16)
        self._cell = {
            'east': 1 if number & 8 else 0,
            'north': 1 if number & 4 else 0,
            'west': 1 if number & 2 else 0,
            'south': 1 if number & 1 else 0,
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
