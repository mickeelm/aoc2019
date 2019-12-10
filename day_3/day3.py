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
