from _collections import deque


class ProgramTerminatedError(Exception):
    pass


class NoInputProvidedError(Exception):
    pass


class IntCode:
    def __init__(self, program):
        self.program = program.copy()
        self.position = 0
        self.input_instructions = deque()
        self.output_values = deque()

    def run(self, suspend_on_output=False):
        while (instruction := self.program[self.position]) != 99:
            opcode, mode_p1, mode_p2 = parse_instruction(instruction)
            if opcode == 3:
                self.input()
                continue
            value_p1 = self.get_value(mode_p1, 1)
            if opcode == 4:
                self.output(value_p1)
                if suspend_on_output:
                    return
                continue
            value_p2 = self.get_value(mode_p2, 2)
            if opcode == 1:
                self.addition(value_p1, value_p2)
            elif opcode == 2:
                self.multiplication(value_p1, value_p2)
            elif opcode == 5:
                self.jump_if_true(value_p1, value_p2)
            elif opcode == 6:
                self.jump_if_false(value_p1, value_p2)
            elif opcode == 7:
                self.less_than(value_p1, value_p2)
            elif opcode == 8:
                self.equals(value_p1, value_p2)
            else:
                raise RuntimeError(f'Unknown opcode: {opcode}')
        return

    def get_value(self, mode, position_offset):
        value = self.program[self.program[self.position + position_offset]] if mode == 0 else self.program[
            self.position + position_offset]
        return value

    def addition(self, value_p1, value_p2):
        self.program[self.program[self.position + 3]] = value_p1 + value_p2
        self.position += 4

    def multiplication(self, value_p1, value_p2):
        self.program[self.program[self.position + 3]] = value_p1 * value_p2
        self.position += 4

    def input(self):
        try:
            self.program[self.program[self.position + 1]] = self.input_instructions.popleft()
            self.position += 2
        except IndexError:
            raise NoInputProvidedError

    def output(self, value_p1):
        self.output_values.append(value_p1)
        self.position += 2

    def jump_if_true(self, value_p1, value_p2):
        self.position = value_p2 if value_p1 else self.position + 3

    def jump_if_false(self, value_p1, value_p2):
        self.position = value_p2 if not value_p1 else self.position + 3

    def less_than(self, value_p1, value_p2):
        self.store_one_or_zero(value_p1 < value_p2)

    def equals(self, value_p1, value_p2):
        self.store_one_or_zero(value_p1 == value_p2)

    def store_one_or_zero(self, store_one):
        self.program[self.program[self.position + 3]] = 1 if store_one else 0
        self.position += 4

    def queue_input(self, value):
        self.input_instructions.append(value)

    def get_last_output(self):
        self.output_values.pop()

    def run_until_output(self):
        if self.output_values:
            return self.output_values.pop()
        self.run(True)
        if self.output_values:
            return self.output_values.pop()
        else:
            raise ProgramTerminatedError


def parse_instruction(instruction):
    opcode = instruction % 10
    param_1_mode = int(instruction / 100) % 10
    param_2_mode = int(instruction / 1000) % 10
    return opcode, param_1_mode, param_2_mode
