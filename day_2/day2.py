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


def brute_force(intcode, output):
    for noun in range(0, 100):
        for verb in range(0, 100):
            copy = intcode.copy()
            copy[1] = noun
            copy[2] = verb
            if process(copy)[0] == output:
                return noun * 100 + verb
