from multiprocessing import Pool

from day_4.day4 import meets_criteria_pt1, meets_criteria_pt2, as_digits


def test_meets_criteria_pt1():
    assert meets_criteria_pt1(111111)
    assert meets_criteria_pt1(223450) is False
    assert meets_criteria_pt1(123789) is False


def test_meets_criteria_pt2():
    assert meets_criteria_pt2(112233)
    assert meets_criteria_pt2(111122)
    assert meets_criteria_pt2(123444) is False
    assert meets_criteria_pt2(124449) is False


def test_as_digits():
    assert as_digits(111111) == (1, 1, 1, 1, 1, 1)
    assert as_digits(123456) == (1, 2, 3, 4, 5, 6)
    assert as_digits(654321) == (6, 5, 4, 3, 2, 1)
    assert as_digits(987654) == (9, 8, 7, 6, 5, 4)


def test_answer_part_1():
    with Pool() as p:
        assert sum(p.map(meets_criteria_pt1, range(137683, 596253))) == 1864


def test_answer_part_2():
    with Pool() as p:
        assert sum(p.map(meets_criteria_pt2, range(137683, 596253))) == 1258
