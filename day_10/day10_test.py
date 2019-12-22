from day_10.day10 import best_location, vaporize_until_200, Asteroid, add_other_degrees_and_positions


def test_best_location():
    with open('example_1') as ex1:
        winner = best_location([line.rstrip() for line in ex1])
        assert winner.position() == (3, 4)
        assert len(winner.unique_degrees) == 8
    with open('example_2') as ex2:
        winner = best_location([line.rstrip() for line in ex2])
        assert winner.position() == (5, 8)
        assert len(winner.unique_degrees) == 33
    with open('example_3') as ex3:
        winner = best_location([line.rstrip() for line in ex3])
        assert winner.position() == (1, 2)
        assert len(winner.unique_degrees) == 35
    with open('example_4') as ex4:
        winner = best_location([line.rstrip() for line in ex4])
        assert winner.position() == (6, 3)
        assert len(winner.unique_degrees) == 41
    with open('example_5') as ex5:
        winner = best_location([line.rstrip() for line in ex5])
        assert winner.position() == (11, 13)
        assert len(winner.unique_degrees) == 210


def test_answer_1():
    with open('input') as inp:
        winner = best_location([line.rstrip() for line in inp])
        assert winner.position() == (27, 19)
        assert len(winner.unique_degrees) == 314


def test_add_other_degrees_and_positions():
    asteroid = Asteroid(10, 10)
    add_other_degrees_and_positions(asteroid, [Asteroid(9, 10)])
    assert asteroid.degrees_and_asteroids.pop() == (180, (9, 10))
    add_other_degrees_and_positions(asteroid, [Asteroid(9, 9)])
    assert asteroid.degrees_and_asteroids.pop() == (135, (9, 9))
    add_other_degrees_and_positions(asteroid, [Asteroid(10, 9)])
    assert asteroid.degrees_and_asteroids.pop() == (90, (10, 9))
    add_other_degrees_and_positions(asteroid, [Asteroid(11, 9)])
    assert asteroid.degrees_and_asteroids.pop() == (45, (11, 9))
    add_other_degrees_and_positions(asteroid, [Asteroid(11, 10)])
    assert asteroid.degrees_and_asteroids.pop() == (0, (11, 10))
    add_other_degrees_and_positions(asteroid, [Asteroid(11, 11)])
    assert asteroid.degrees_and_asteroids.pop() == (-45, (11, 11))
    add_other_degrees_and_positions(asteroid, [Asteroid(10, 11)])
    assert asteroid.degrees_and_asteroids.pop() == (-90, (10, 11))
    add_other_degrees_and_positions(asteroid, [Asteroid(9, 11)])
    assert asteroid.degrees_and_asteroids.pop() == (-135, (9, 11))


def test_vaporize_until_200():
    with open('example_5') as ex5:
        assert vaporize_until_200([line.rstrip() for line in ex5]) == 802


def test_answer_2():
    with open('input') as inp:
        assert vaporize_until_200([line.rstrip() for line in inp]) == 1513
