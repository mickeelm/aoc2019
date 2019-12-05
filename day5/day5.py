def process(intcode, input_val=None):
    position = 0
    output = []
    while (instruction := intcode[position]) != 99:
        opcode, mode_p1, mode_p2 = parse_instruction(instruction)
        if opcode == 3:
            intcode[intcode[position + 1]] = input_val
            position += 2
            continue

        value_p1 = intcode[intcode[position + 1]] if mode_p1 == 0 else intcode[position + 1]
        if opcode == 4:
            output.append(value_p1)
            position += 2
            continue

        value_p2 = intcode[intcode[position + 2]] if mode_p2 == 0 else intcode[position + 2]
        if (addition := opcode == 1) or opcode == 2:
            intcode[intcode[position + 3]] = value_p1 + value_p2 if addition else value_p1 * value_p2
            position += 4
            continue
        if (jump_if_true := opcode == 5) or opcode == 6:
            jump_if_false = not jump_if_true
            if (jump_if_true and value_p1) or (jump_if_false and not value_p1):
                position = value_p2
            else:
                position += 3
            continue
        if (less_than := opcode == 7) or opcode == 8:
            equals = not less_than
            store_one = (less_than and value_p1 < value_p2) or (equals and value_p1 == value_p2)
            intcode[intcode[position + 3]] = 1 if store_one else 0
            position += 4
            continue
        raise RuntimeError(f'Unknown opcode: {opcode}')
    return intcode, output


def parse_instruction(instruction):
    opcode = instruction % 10
    param_1_mode = int(instruction / 100) % 10
    param_2_mode = int(instruction / 1000) % 10
    return opcode, param_1_mode, param_2_mode


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
