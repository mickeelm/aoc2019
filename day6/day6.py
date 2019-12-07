def init_map(raw_entries):
    objects = ObjectDict()
    for entry in raw_entries:
        base_name, orbiter_name = entry.split(')')
        base = objects[base_name]
        orbiter = objects[orbiter_name]
        base.add_orbiter(orbiter)
        orbiter.base = base
    return objects


def checksum(map_entries):
    com = next(filter(lambda x: x.base is None, map_entries.values()))
    set_orbits(com.orbiters, 0)
    return sum([x.orbits for x in map_entries.values()])


def set_orbits(orbiters, indirect_orbits):
    for obj in orbiters:
        obj.orbits = indirect_orbits + 1
        set_orbits(obj.orbiters, obj.orbits)


def orbital_transfer(map_entries, start_id, goal_id):
    start_obj = map_entries[start_id]
    goal_obj = map_entries[goal_id]
    start_path = []
    goal_path = []
    while True:
        start_obj = start_obj.base if start_obj.base else start_obj
        goal_obj = goal_obj.base if goal_obj.base else goal_obj
        start_path.append(start_obj.name)
        goal_path.append(goal_obj.name)
        common = list(set(start_path) & set(goal_path))
        if common:
            return start_path.index(common[0]) + goal_path.index(common[0])


class Object:
    def __init__(self, name):
        self.name = name
        self.base = None
        self.orbits = 0
        self.orbiters = []

    def add_orbiter(self, orbiter):
        self.orbiters.append(orbiter)

    def __repr__(self):
        return self.name


class ObjectDict(dict):
    def __missing__(self, key):
        obj = Object(key)
        self[key] = obj
        return obj


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
