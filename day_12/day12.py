from itertools import combinations


def total_energy_level(moons, steps):
    moons = take_steps(moons, steps)
    return sum([energy_level(moon) for moon in moons])


def energy_level(moon):
    pot = abs(moon.pos_x) + abs(moon.pos_y) + abs(moon.pos_z)
    kin = abs(moon.vel_x) + abs(moon.vel_y) + abs(moon.vel_z)
    return pot * kin


def take_steps(moons, steps):
    for step in range(steps):
        pairs = combinations(moons, 2)
        for pair in pairs:
            adjust_velocity(pair)
        for moon in moons:
            moon.take_step()
    return moons


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


def adjust_velocity(pair):
    a, b = pair
    x = velocity_change(a.pos_x, b.pos_x)
    y = velocity_change(a.pos_y, b.pos_y)
    z = velocity_change(a.pos_z, b.pos_z)
    a.vel_x += x
    a.vel_y += y
    a.vel_z += z
    b.vel_x -= x
    b.vel_y -= y
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
