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
