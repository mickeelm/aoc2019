from common.intcode import IntCode


def boost_keycode(program, input_value):
    computer = IntCode(program)
    if input_value:
        computer.queue_input(input_value)
    computer.run()
    return list(computer.output_values)
