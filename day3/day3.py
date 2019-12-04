def closest_intersections(first_wire, second_wire):
    least_no_of_steps = None
    shortest_mh_distance = None

    steps_taken_first = 0
    point_a_first = (0, 0)
    for instr_first in first_wire:
        point_b_first, steps_to_b_first = next_point(point_a_first, instr_first)
        steps_taken_second = 0
        point_a_second = (0, 0)
        for instr_second in second_wire:
            point_b_second, steps_to_b_second = next_point(point_a_second, instr_second)
            if intersection_coords := intersection((point_a_first, point_b_first), (point_a_second, point_b_second)):
                x, y = intersection_coords
                mh_distance = abs(x) + abs(y)
                steps = steps_taken_first + steps_taken_second + steps_to_intersection(intersection_coords,
                                                                                       point_a_first, point_a_second)
                if not shortest_mh_distance or mh_distance < shortest_mh_distance:
                    shortest_mh_distance = mh_distance
                if not least_no_of_steps or steps < least_no_of_steps:
                    least_no_of_steps = steps
            point_a_second = point_b_second
            steps_taken_second += steps_to_b_second
        point_a_first = point_b_first
        steps_taken_first += steps_to_b_first

    return shortest_mh_distance, least_no_of_steps


def next_point(point, instruction):
    x, y = point
    direction = instruction[:1]
    distance = int(instruction[1:])

    if direction == 'U':
        y += distance
    elif direction == 'R':
        x += distance
    elif direction == 'D':
        y -= distance
    elif direction == 'L':
        x -= distance
    return (x, y), distance


def intersection(line1, line2):
    line1_horizontal = line1[0][1] == line1[1][1]
    line2_horizontal = line2[0][1] == line2[1][1]

    if line1_horizontal == line2_horizontal:
        return None

    horizontal_line = line1 if line1_horizontal else line2
    vertical_line = line1 if line2_horizontal else line2

    horizontal_p1, horizontal_p2 = horizontal_line
    vertical_p1, vertical_p2 = vertical_line
    horizontal_y = horizontal_p1[1]
    vertical_x = vertical_p1[0]

    if vertical_x == 0 and horizontal_y == 0:
        return None

    horizontal_min_x = min(horizontal_p1[0], horizontal_p2[0])
    horizontal_max_x = max(horizontal_p1[0], horizontal_p2[0])
    vertical_min_y = min(vertical_p1[1], vertical_p2[1])
    vertical_max_y = max(vertical_p1[1], vertical_p2[1])

    horizontal_align = vertical_min_y <= horizontal_y <= vertical_max_y
    vertical_align = horizontal_min_x <= vertical_x <= horizontal_max_x

    return (vertical_x, horizontal_y) if vertical_align and horizontal_align else None


def steps_to_intersection(intersection_coords, previous_point_first, previous_point_second):
    int_x, int_y = intersection_coords
    first_x, first_y = previous_point_first
    second_x, second_y = previous_point_second
    if first_x == int_x:
        return abs(abs(int_y) - abs(first_y)) + abs(abs(int_x) - abs(second_x))
    else:
        return abs(abs(int_x) - abs(first_x)) + abs(abs(int_y) - abs(second_y))


# TESTS #

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
