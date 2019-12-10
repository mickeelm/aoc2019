from day_5.day5 import process


def test_process():
    # tests from day 2 that should still work, and have an empty output list
    assert process([1, 0, 0, 0, 99]) == ([2, 0, 0, 0, 99], [])
    assert process([2, 3, 0, 3, 99]) == ([2, 3, 0, 6, 99], [])
    assert process([2, 4, 4, 5, 99, 0]) == ([2, 4, 4, 5, 99, 9801], [])
    assert process([1, 1, 1, 4, 99, 5, 6, 0, 99]) == ([30, 1, 1, 4, 2, 5, 6, 0, 99], [])
    # new tests part 1
    assert process([3, 0, 4, 0, 99], 25) == ([25, 0, 4, 0, 99], [25])
    assert process([1002, 4, 3, 4, 33]) == ([1002, 4, 3, 4, 99], [])
    # new tests part 2
    test_input = [int(x) for x in '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,'
                                  '20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99'.split(',')]
    assert process(test_input, 6)[1] == [999]
    assert process(test_input, 8)[1] == [1000]
    assert process(test_input, 10)[1] == [1001]


def test_answer_1():
    with open('input') as f:
        assert process([int(x) for x in f.readline().split(',')], 1)[1] == [0, 0, 0, 0, 0, 0, 0, 0, 0, 4601506]


def test_answer_2():
    with open('input') as f:
        assert process([int(x) for x in f.readline().split(',')], 5)[1] == [5525561]
