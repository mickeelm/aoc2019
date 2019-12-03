def process(intcode):
    position = 0
    while (code := intcode[position]) != 99:
        input_pos_1 = intcode[position + 1]
        input_pos_2 = intcode[position + 2]
        output_pos = intcode[position + 3]
        if code == 1:
            intcode[output_pos] = intcode[input_pos_1] + intcode[input_pos_2]
        else:
            intcode[output_pos] = intcode[input_pos_1] * intcode[input_pos_2]
        position += 4
    return intcode


def brute_force(intcode, ouput):
    for noun in range(0, 100):
        for verb in range(0, 100):
            copy = intcode.copy()
            copy[1] = noun
            copy[2] = verb
            if process(copy)[0] == ouput:
                return noun * 100 + verb


def test_process():
    assert process([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert process([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert process([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert process([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]


def test_answer_1():
    with open('input') as f:
        input = f.readline()
        intcode = [int(code) for code in input.split(',')]
        intcode[1] = 12
        intcode[2] = 2
        assert process(intcode)[0] == 3101844


def test_answer_2():
    with open('input') as f:
        inputcode_raw = f.readline()
        intcode = [int(code) for code in inputcode_raw.split(',')]
        assert brute_force(intcode, 19690720) == 8478
