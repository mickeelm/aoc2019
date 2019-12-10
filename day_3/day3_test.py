from day_3.day3 import intersection, closest_intersections


def test_intersection():
    assert intersection(((10, 4), (10, -4)), ((1, 1), (11, 1))) == (10, 1)
    assert intersection(((-10, 4), (-10, -4)), ((2, 1), (-12, 1))) == (-10, 1)
    assert intersection(((-10, 4), (10, 4)), ((3, 3), (3, 7))) == (3, 4)
    assert intersection(((10, -4), (-10, -4)), ((-8, -8), (-8, -4))) == (-8, -4)
    assert intersection(((10, 4), (10, -4)), ((1, 2), (1, 9))) is None
    assert intersection(((-10, 4), (-10, -4)), ((2, 1), (2, 9))) is None
    assert intersection(((-10, 4), (10, 4)), ((3, 3), (7, 3))) is None
    assert intersection(((10, -4), (-10, -4)), ((2, 1), (2, 9))) is None
    assert intersection(((10, -4), (-10, -4)), ((10, 1), (-10, 1))) is None
    assert intersection(((10, 7), (10, -4)), ((1, 1), (1, 7))) is None


def test_shortest_mh_distance():
    # Examples part 1
    assert closest_intersections('R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(','),
                                 'U62,R66,U55,R34,D71,R55,D58,R83'.split(','))[0] == 159
    assert closest_intersections('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(','),
                                 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(','))[0] == 135


def test_least_steps_to_intersection():
    # Examples part 2
    assert closest_intersections('R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(','),
                                 'U62,R66,U55,R34,D71,R55,D58,R83'.split(','))[1] == 610
    assert closest_intersections('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(','),
                                 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(','))[1] == 410


def test_answer_1_and_2():
    with open('input') as f:
        first = f.readline().strip().split(',')
        second = f.readline().strip().split(',')
        assert closest_intersections(first, second) == (2129, 134662)
