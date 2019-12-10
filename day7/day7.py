from itertools import permutations, cycle

from common.intcode import IntCode, ProgramTerminatedError


def max_thruster_single_mode(program, phase_settings):
    output = 0
    for phase in phase_settings:
        computer = IntCode(program)
        computer.queue_input(phase)
        computer.queue_input(output)
        output = computer.run_until_output()
    return output


def max_thruster_loop_mode(program, phase_settings):
    last_amp_phase = phase_settings[-1]
    last_amp_output = 0
    amps = {phase_setting: IntCode(program) for phase_setting in phase_settings}
    for phase_setting, amp in amps.items():
        amp.queue_input(phase_setting)
    output_signal = 0
    amp_loop = cycle(amps)
    for phase_setting in amp_loop:
        amp_program = amps[phase_setting]
        amp_program.queue_input(output_signal)
        try:
            output_signal = amp_program.run_until_output()
            if phase_setting == last_amp_phase:
                last_amp_output = output_signal
        except ProgramTerminatedError:
            return last_amp_output


def test_max_thruster_single_mode():
    assert max_thruster_single_mode([3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0],
                                    [4, 3, 2, 1, 0]) == 43210
    assert max_thruster_single_mode(
        [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0],
        [0, 1, 2, 3, 4]) == 54321
    assert max_thruster_single_mode(
        [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33, 1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31,
         31, 4, 31, 99, 0, 0, 0], [1, 0, 4, 3, 2]) == 65210


def test_part_1():
    with open('input') as f:
        program = [int(x) for x in f.read().split(',')]
        phase_settings = permutations([0, 1, 2, 3, 4])
        assert max([max_thruster_single_mode(program, phase_setting) for phase_setting in phase_settings]) == 24625


def test_max_thruster_loop_mode():
    assert max_thruster_loop_mode(
        [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0,
         5], [9, 8, 7, 6, 5]) == 139629729
    assert max_thruster_loop_mode(
        [3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54, -5, 54, 1105, 1, 12, 1,
         53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4, 53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0,
         0, 10], [9, 7, 8, 5, 6]) == 18216


def test_part_2():
    with open('input') as f:
        program = [int(x) for x in f.read().split(',')]
        phase_settings = permutations([5, 6, 7, 8, 9])
        assert max([max_thruster_loop_mode(program, phase_setting) for phase_setting in phase_settings]) == 36497698
