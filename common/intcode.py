from _collections import deque, defaultdict


class ProgramTerminatedError(Exception):
    pass


class NoInputProvidedError(Exception):
    pass


class IntCode:

    def __init__(self, program):
        self.program = program.copy()
        self.program_memory_size = len(self.program)
        # noinspection PyArgumentList
        self.extended_memory = defaultdict(int)
        self.position = 0
        self.base_offset = 0
        self.operations = self.init_operations()
        self.input_instructions = deque()
        self.output_values = deque()

    def init_operations(self):
        operations = {1: self.addition, 2: self.multiplication, 3: self.input, 4: self.output, 5: self.jump_if_true,
                      6: self.jump_if_false, 7: self.less_than, 8: self.equals, 9: self.adjust_base}
        return operations

    def run(self, suspend_on_output=False):
        while (instruction := self.program[self.position]) != 99:
            opcode = instruction % 10
            func_call = self.operations[opcode]
            func_call(instruction)
            if opcode == 4 and suspend_on_output:
                return
        return

    def addition(self, instruction):
        self.store_func_of_two_values(instruction, lambda x, y: x + y)

    def multiplication(self, instruction):
        self.store_func_of_two_values(instruction, lambda x, y: x * y)

    def store_func_of_two_values(self, instruction, function):
        value_p1, value_p2, store_pos = self.get_two_values_and_store_pos(instruction)
        self.store(store_pos, function(value_p1, value_p2))
        self.position += 4

    def input(self, instruction):
        mode_p1 = parse_instruction(instruction, 1)
        store_pos = self.get_store_pos(mode_p1, 1)
        try:
            self.store(store_pos, self.input_instructions.popleft())
            self.position += 2
        except IndexError:
            raise NoInputProvidedError

    def output(self, instruction):
        value_p1 = self.get_one_value(instruction)
        self.output_values.append(value_p1)
        self.position += 2

    def jump_if_true(self, instruction):
        self.jump(instruction, lambda x: x)

    def jump_if_false(self, instruction):
        self.jump(instruction, lambda x: not x)

    def jump(self, instruction, function):
        value_p1, value_p2 = self.get_two_values(instruction)
        self.position = value_p2 if function(value_p1) else self.position + 3

    def less_than(self, instruction):
        self.store_one_or_zero(instruction, lambda x, y: x < y)

    def equals(self, instruction):
        self.store_one_or_zero(instruction, lambda x, y: x == y)

    def store_one_or_zero(self, instruction, function):
        value_p1, value_p2, store_pos = self.get_two_values_and_store_pos(instruction)
        self.store(store_pos, 1 if function(value_p1, value_p2) else 0)
        self.position += 4

    def adjust_base(self, instruction):
        value_p1 = self.get_one_value(instruction)
        self.base_offset += value_p1
        self.position += 2

    def get_value(self, mode, position_offset):
        value_at_pos = self.program[self.position + position_offset]
        if mode == 0:
            return self.program[value_at_pos] if value_at_pos < self.program_memory_size else \
                self.extended_memory[value_at_pos]
        elif mode == 1:
            return value_at_pos
        elif mode == 2:
            value_base_offset_adj = self.base_offset + value_at_pos
            return self.program[value_base_offset_adj] if value_base_offset_adj < self.program_memory_size else \
                self.extended_memory[value_base_offset_adj]

    def store(self, store_pos, value):
        if store_pos < self.program_memory_size:
            self.program[store_pos] = value
        else:
            self.extended_memory[store_pos] = value

    def get_store_pos(self, mode, position_offset):
        if mode == 0:
            return self.program[self.position + position_offset]
        elif mode == 2:
            return self.base_offset + self.program[self.position + position_offset]

    def get_one_value(self, instruction):
        mode_p1 = parse_instruction(instruction, 1)
        value_p1 = self.get_value(mode_p1, 1)
        return value_p1

    def get_two_values(self, instruction):
        mode_p1, mode_p2 = parse_instruction(instruction, 2)
        value_p1 = self.get_value(mode_p1, 1)
        value_p2 = self.get_value(mode_p2, 2)
        return value_p1, value_p2

    def get_two_values_and_store_pos(self, instruction):
        mode_p1, mode_p2, mode_p3 = parse_instruction(instruction)
        value_p1 = self.get_value(mode_p1, 1)
        value_p2 = self.get_value(mode_p2, 2)
        store_pos = self.get_store_pos(mode_p3, 3)
        return value_p1, value_p2, store_pos

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


def parse_instruction(instruction, modes_required=3):
    param_1_mode = int(instruction / 100) % 10
    if modes_required == 1:
        return param_1_mode
    param_2_mode = int(instruction / 1000) % 10
    if modes_required == 2:
        return param_1_mode, param_2_mode
    param_3_mode = int(instruction / 10000) % 10
    return param_1_mode, param_2_mode, param_3_mode
