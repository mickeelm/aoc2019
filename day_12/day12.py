from copy import deepcopy
from multiprocessing.pool import Pool

from itertools import combinations
from math import gcd


def first_repeat_step(moons):
    x = (pos_x, adjust_velocity_x, deepcopy(moons))
    y = (pos_y, adjust_velocity_y, deepcopy(moons))
    z = (pos_z, adjust_velocity_z, deepcopy(moons))

    pool = Pool()
    repeat_indexes = pool.map(find_repeat_index, [x, y, z])
    return reduce_lcms(repeat_indexes)


def find_repeat_index(functions_and_moons):
    pos_func, adj_func, moons = functions_and_moons
    moon = moons[0]
    seq = SequenceMatcher(15)

    steps = 0
    while True:
        if seq.match_found(pos_func(moon)):
            return steps - 14
        take_step(moons, adj_func)
        steps += 1


def reduce_lcms(repeat_indexes):
    combos = combinations(repeat_indexes, 2)
    reduced = set([lcm(x, y) for x, y in combos])

    if len(reduced) > 1:
        return reduce_lcms(reduced)
    return reduced.pop()


def lcm(x, y):
    return x * y // gcd(x, y)


class SequenceMatcher:
    def __init__(self, sync_length):
        self.sync_length = sync_length
        self.sequence = []
        self.sequence_initialized = False
        self.pos_to_match = 0

    def match_found(self, value):
        if not self.sequence_initialized:
            self.sequence.append(value)
            if len(self.sequence) == self.sync_length:
                self.sequence_initialized = True
            return False

        if self.sequence[self.pos_to_match] == value:
            self.pos_to_match += 1
            return self.pos_to_match == self.sync_length

        self.pos_to_match = 0
        if self.sequence[0] == value:
            self.pos_to_match = 1
        return False


def total_energy_level(moons, steps):
    moons = take_steps(moons, steps)
    return sum([energy_level(moon) for moon in moons])


def energy_level(moon):
    pot = abs(moon.pos_x) + abs(moon.pos_y) + abs(moon.pos_z)
    kin = abs(moon.vel_x) + abs(moon.vel_y) + abs(moon.vel_z)
    return pot * kin


def take_steps(moons, steps):
    for step in range(steps):
        take_step(moons)
    return moons


def take_step(moons, adj_func=None):
    pairs = combinations(moons, 2)
    for pair in pairs:
        if adj_func:
            adj_func(pair)
        else:
            adjust_velocity(pair)
    for moon in moons:
        moon.take_step()


class Moon:
    def __init__(self, raw_moon):
        pos, vel = parse_positions_and_velocities(raw_moon)
        self.pos_x, self.pos_y, self.pos_z = pos
        self.vel_x, self.vel_y, self.vel_z = vel

    def take_step(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        self.pos_z += self.vel_z

    def __eq__(self, other):
        if self.pos_x != other.pos_x:
            return False
        if self.pos_y != other.pos_y:
            return False
        if self.pos_z != other.pos_z:
            return False
        if self.vel_x != other.vel_x:
            return False
        if self.vel_y != other.vel_y:
            return False
        if self.vel_z != other.vel_z:
            return False
        return True

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return f'pos:<{self.pos_x},{self.pos_y},{self.pos_z}> vel:<{self.vel_x},{self.vel_y},{self.vel_z}>'


def pos_x(moon):
    return moon.pos_x


def pos_y(moon):
    return moon.pos_y


def pos_z(moon):
    return moon.pos_z


def adjust_velocity(pair):
    adjust_velocity_x(pair)
    adjust_velocity_y(pair)
    adjust_velocity_z(pair)


def adjust_velocity_x(pair):
    a, b = pair
    x = velocity_change(a.pos_x, b.pos_x)
    a.vel_x += x
    b.vel_x -= x


def adjust_velocity_y(pair):
    a, b = pair
    y = velocity_change(a.pos_y, b.pos_y)
    a.vel_y += y
    b.vel_y -= y


def adjust_velocity_z(pair):
    a, b = pair
    z = velocity_change(a.pos_z, b.pos_z)
    a.vel_z += z
    b.vel_z -= z


def velocity_change(own_pos, other_pos):
    if own_pos < other_pos:
        return 1
    if own_pos > other_pos:
        return -1
    return 0


def parse_positions_and_velocities(raw):
    is_init = 'pos' not in raw
    if is_init:
        return parse_xyz(raw), [0, 0, 0]
    pos_raw, vel_raw = raw.split(', vel=')
    pos_raw = pos_raw.split('pos=')[1]

    return parse_xyz(pos_raw), parse_xyz(vel_raw)


def parse_xyz(raw):
    return [int(axis.split('=')[1]) for axis in raw[1:-1].split(', ')]
