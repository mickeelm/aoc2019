from enum import Enum

from common.intcode import IntCode, ProgramTerminatedError


def next_panel(panel, direction):
    if direction == Direction.UP:
        return panel.x, panel.y + 1
    if direction == Direction.RIGHT:
        return panel.x + 1, panel.y
    if direction == Direction.DOWN:
        return panel.x, panel.y - 1
    return panel.x - 1, panel.y


def rotate(direction, dir_value):
    if direction == Direction.UP:
        return Direction.LEFT if not dir_value else Direction.RIGHT
    if direction == Direction.RIGHT:
        return Direction.UP if not dir_value else Direction.DOWN
    if direction == Direction.DOWN:
        return Direction.RIGHT if not dir_value else Direction.LEFT
    return Direction.DOWN if not dir_value else Direction.UP


def count_painted_panels(program):
    panels = paint_panels(program)
    return sum(panel.painted for panel in panels.values())


def print_panels(program):
    panels = paint_panels(program, True)
    min_x = min(panels.keys(), key=lambda key: key[0])[0]
    max_x = max(panels.keys(), key=lambda key: key[0])[0]
    min_y = min(panels.keys(), key=lambda key: key[1])[1]
    max_y = max(panels.keys(), key=lambda key: key[1])[1]

    print()
    for y in range(max_y, min_y - 1, -1):
        for x in range(min_x, max_x + 1):
            panel = panels[(x, y)]
            print('█', end='') if panel.color == 1 else print(' ', end='')
        print()
    return True


def paint_panels(program, paint_first_white=False):
    panels = PanelDict()
    ic = IntCode(program)
    current = panels[(0, 0)]
    if paint_first_white:
        current.paint(1)
    direction = Direction.UP
    while True:
        try:
            ic.queue_input(current.color)
            color = ic.run_until_output()
            current.paint(color)
            dir_value = ic.run_until_output()
            direction = rotate(direction, dir_value)
            current = panels[next_panel(current, direction)]
        except ProgramTerminatedError:
            break
    return panels


class Panel:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = 0
        self.painted = False

    def paint(self, color):
        self.color = color
        self.painted = True


class PanelDict(dict):
    def __missing__(self, key):
        panel = Panel(*key)
        self[key] = panel
        return panel


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4
