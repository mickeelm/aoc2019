from day_11.day11 import Panel, next_panel, Direction, rotate, count_painted_panels, print_panels


def test_next_panel():
    assert next_panel(Panel(0, 0), Direction.UP) == (0, 1)
    assert next_panel(Panel(0, 0), Direction.RIGHT) == (1, 0)
    assert next_panel(Panel(0, 0), Direction.DOWN) == (0, -1)
    assert next_panel(Panel(0, 0), Direction.LEFT) == (-1, 0)


def test_rotate():
    assert rotate(Direction.UP, 0) == Direction.LEFT
    assert rotate(Direction.UP, 1) == Direction.RIGHT
    assert rotate(Direction.RIGHT, 0) == Direction.UP
    assert rotate(Direction.RIGHT, 1) == Direction.DOWN
    assert rotate(Direction.DOWN, 0) == Direction.RIGHT
    assert rotate(Direction.DOWN, 1) == Direction.LEFT
    assert rotate(Direction.LEFT, 0) == Direction.DOWN
    assert rotate(Direction.LEFT, 1) == Direction.UP


def test_part_1():
    with open('input') as f:
        assert count_painted_panels([int(instr) for instr in f.readline().split(',')]) == 1732


def test_part_2():
    with open('input') as f:
        assert print_panels([int(instr) for instr in f.readline().split(',')])
