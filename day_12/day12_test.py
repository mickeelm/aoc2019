from day_12.day12 import Moon, take_steps, total_energy_level


def test_answer_1():
    with open('input') as start_stream:
        start_state = [Moon(line.rstrip()) for line in start_stream.readlines()]
    assert total_energy_level(start_state, 1000) == 12466


def test_energy_level_input_1():
    with open('test_inputs/test_input_1') as start_stream:
        start_state = [Moon(line.rstrip()) for line in start_stream.readlines()]
    assert total_energy_level(start_state, 10) == 179


def test_energy_level_input_2():
    with open('test_inputs/test_input_2') as start_stream:
        start_state = [Moon(line.rstrip()) for line in start_stream.readlines()]
    assert total_energy_level(start_state, 100) == 1940


def test_take_steps():
    helper_take_steps('test_inputs/test_input_1', 'test_inputs/test_input_1_1_step', 1)
    helper_take_steps('test_inputs/test_input_1', 'test_inputs/test_input_1_2_steps', 2)
    helper_take_steps('test_inputs/test_input_1', 'test_inputs/test_input_1_3_steps', 3)
    helper_take_steps('test_inputs/test_input_1', 'test_inputs/test_input_1_4_steps', 4)
    helper_take_steps('test_inputs/test_input_1', 'test_inputs/test_input_1_5_steps', 5)
    helper_take_steps('test_inputs/test_input_1', 'test_inputs/test_input_1_6_steps', 6)
    helper_take_steps('test_inputs/test_input_1', 'test_inputs/test_input_1_7_steps', 7)
    helper_take_steps('test_inputs/test_input_1', 'test_inputs/test_input_1_8_steps', 8)
    helper_take_steps('test_inputs/test_input_1', 'test_inputs/test_input_1_9_steps', 9)
    helper_take_steps('test_inputs/test_input_1', 'test_inputs/test_input_1_10_steps', 10)
    helper_take_steps('test_inputs/test_input_2', 'test_inputs/test_input_2_10_steps', 10)
    helper_take_steps('test_inputs/test_input_2', 'test_inputs/test_input_2_20_steps', 20)
    helper_take_steps('test_inputs/test_input_2', 'test_inputs/test_input_2_30_steps', 30)
    helper_take_steps('test_inputs/test_input_2', 'test_inputs/test_input_2_40_steps', 40)
    helper_take_steps('test_inputs/test_input_2', 'test_inputs/test_input_2_50_steps', 50)
    helper_take_steps('test_inputs/test_input_2', 'test_inputs/test_input_2_60_steps', 60)
    helper_take_steps('test_inputs/test_input_2', 'test_inputs/test_input_2_70_steps', 70)
    helper_take_steps('test_inputs/test_input_2', 'test_inputs/test_input_2_80_steps', 80)
    helper_take_steps('test_inputs/test_input_2', 'test_inputs/test_input_2_90_steps', 90)
    helper_take_steps('test_inputs/test_input_2', 'test_inputs/test_input_2_100_steps', 100)


def helper_take_steps(start_file, end_file, no_of_steps):
    with open(start_file) as start_stream, open(end_file) as end_stream:
        start_state = [Moon(line.rstrip()) for line in start_stream.readlines()]
        end_state = [Moon(line.rstrip()) for line in end_stream.readlines()]
        assert take_steps(start_state, no_of_steps) == end_state
