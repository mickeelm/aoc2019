from day_9.day9 import boost_keycode


def test_boost_keycode():
    quine = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    assert boost_keycode(quine, None) == quine
    assert boost_keycode([1102, 34915192, 34915192, 454545, 4, 454545, 99, 0], None) == [1219070632396864]
    assert boost_keycode([104, 1125899906842624, 99], None) == [1125899906842624]


def test_part_1():
    with open('input') as f:
        assert boost_keycode([int(instr) for instr in f.readline().split(',')], 1) == [2745604242]


def test_part_2():
    with open('input') as f:
        assert boost_keycode([int(instr) for instr in f.readline().split(',')], 2) == [51135]
