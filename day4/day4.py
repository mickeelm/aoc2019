def as_digits(number):
    one = number % 10
    ten = int(number / 10) % 10
    hun = int(number / 100) % 10
    tho = int(number / 1000) % 10
    t_tho = int(number / 10000) % 10
    h_tho = int(number / 100000)

    return h_tho, t_tho, tho, hun, ten, one


def meets_criteria_pt1(digits):
    if decreases(digits):
        return False
    if has_multiple(digits):
        return True
    return False


def meets_criteria_pt2(digits):
    if decreases(digits):
        return False
    if has_double(digits):
        return True
    return False


def has_multiple(digits):
    h_tho, t_tho, tho, hun, ten, one = digits
    if h_tho == t_tho or t_tho == tho or tho == hun or hun == ten or ten == one:
        return True


def has_double(digits):
    h_tho, t_tho, tho, hun, ten, one = digits
    if h_tho == t_tho and t_tho != tho:
        return True
    if t_tho == tho and tho != hun and t_tho != h_tho:
        return True
    if tho == hun and hun != ten and tho != t_tho:
        return True
    if hun == ten and ten != one and hun != tho:
        return True
    if ten == one and ten != hun:
        return True
    return False


def decreases(digits):
    h_tho, t_tho, tho, hun, ten, one = digits
    if t_tho < h_tho or tho < t_tho or hun < tho or ten < hun or one < ten:
        return True
    return False


def test_meets_criteria_pt1():
    assert meets_criteria_pt1(as_digits(111111))
    assert meets_criteria_pt1(as_digits(223450)) is False
    assert meets_criteria_pt1(as_digits(123789)) is False


def test_meets_criteria_pt2():
    assert meets_criteria_pt2(as_digits(112233))
    assert meets_criteria_pt2(as_digits(111122))
    assert meets_criteria_pt2(as_digits(123444)) is False
    assert meets_criteria_pt2(as_digits(124449)) is False


def test_as_digits():
    assert as_digits(111111) == (1, 1, 1, 1, 1, 1)
    assert as_digits(123456) == (1, 2, 3, 4, 5, 6)
    assert as_digits(654321) == (6, 5, 4, 3, 2, 1)
    assert as_digits(987654) == (9, 8, 7, 6, 5, 4)


def test_answer_part_1():
    passwords = 0
    for number in range(137683, 596253):
        if meets_criteria_pt1(as_digits(number)):
            passwords += 1
    assert passwords == 1864


def test_answer_part_2():
    passwords = 0
    for number in range(137683, 596253):
        if meets_criteria_pt2(as_digits(number)):
            passwords += 1
    assert passwords == 1258
