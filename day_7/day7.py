from itertools import cycle

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
