from collections import deque
from functools import cmp_to_key

from math import atan2, degrees


def best_location(map_rows):
    asteroids = []
    for y, row in enumerate(map_rows):
        for x, x_val in enumerate(row):
            if x_val == '#':
                asteroids.append(Asteroid(x, y))

    for asteroid in asteroids:
        add_other_degrees_and_positions(asteroid, asteroids)

    best = max(asteroids, key=lambda ast: len(ast.unique_degrees))
    return best


def vaporize_until_200(map_rows):
    location = best_location(map_rows)
    sorted_asteroids = deque(sorted(location.degrees_and_asteroids, key=cmp_to_key(asteroid_cmp)))
    while sorted_asteroids[-1][0] > 90:
        sorted_asteroids.rotate(1)
    last = sorted_asteroids.pop()
    vaporize_count = 1
    while True:
        if vaporize_count == 200:
            x, y = last[1]
            return x * 100 + y
        if sorted_asteroids[-1][0] == last[0]:
            sorted_asteroids.rotate(1)
            continue
        last = sorted_asteroids.pop()
        vaporize_count += 1
    pass


def add_other_degrees_and_positions(asteroid, other_asteroids):
    x, y = asteroid.position()
    for other in other_asteroids:
        if other is asteroid:
            continue
        other_x, other_y = other.position()
        dgr = degrees(atan2(y - other_y, other_x - x))
        asteroid.append_other_degrees_and_asteroid(dgr, other.position())
    pass


def asteroid_cmp(a, b):
    a_degrees, a_asteroid = a
    b_degrees, b_asteroid = b
    if a_degrees < b_degrees:
        return -1
    if a_degrees > b_degrees:
        return 1
    a_x, a_y = a_asteroid
    b_x, b_y = b_asteroid
    x_delta = b_x - a_x
    y_delta = a_y - b_y
    int_dgr = int(a_degrees)

    if 0 < int_dgr < 180:
        return 1 if y_delta > 0 else -1
    if -180 < int_dgr < 0:
        return 1 if y_delta < 0 else -1
    if int_dgr == 0:
        return 1 if x_delta > 0 else -1
    if int_dgr == 180:
        return 1 if x_delta < 0 else -1
    raise RuntimeError('Identical asteroids!')


class Asteroid:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.degrees_and_asteroids = []
        self.unique_degrees = set()

    def position(self):
        return self.x, self.y

    def append_other_degrees_and_asteroid(self, degree, asteroid):
        self.degrees_and_asteroids.append((degree, asteroid))
        self.unique_degrees.add(degree)
