from day_6.day6 import init_map, checksum, orbital_transfer


def test_checksum():
    with open('test_input') as f:
        orbit_map = init_map([x.rstrip() for x in f.readlines()])
        assert checksum(orbit_map) == 42


def test_answer_1():
    with open('input') as f:
        orbit_map = init_map([x.rstrip() for x in f.readlines()])
        assert checksum(orbit_map) == 292387


def test_orbital_transfer():
    with open('test_input_2') as f:
        orbit_map = init_map([x.rstrip() for x in f.readlines()])
        assert orbital_transfer(orbit_map, 'YOU', 'SAN') == 4


def test_answer_2():
    with open('input') as f:
        orbit_map = init_map([x.rstrip() for x in f.readlines()])
        assert orbital_transfer(orbit_map, 'YOU', 'SAN') == 433
