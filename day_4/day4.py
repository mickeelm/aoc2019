def as_digits(number):
    one = number % 10
    ten = int(number / 10) % 10
    hun = int(number / 100) % 10
    tho = int(number / 1000) % 10
    t_tho = int(number / 10000) % 10
    h_tho = int(number / 100000)

    return h_tho, t_tho, tho, hun, ten, one


def meets_criteria_pt1(number):
    digits = as_digits(number)
    if decreases(digits):
        return False
    if has_multiple(digits):
        return True
    return False


def meets_criteria_pt2(number):
    digits = as_digits(number)
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
