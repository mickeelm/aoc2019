def fuel_required_single_module(mass):
    fuel = int(mass / 3) - 2
    return fuel if fuel > 0 else 0


def fuel_required_multiple_modules(masses):
    total_fuel = 0
    for mass in masses:
        total_fuel += fuel_required_single_module(mass)
    return total_fuel


def recursive_fuel_required_single_module(mass):
    total_fuel = 0
    while mass := fuel_required_single_module(mass):
        total_fuel += mass
    return total_fuel


def recursive_fuel_required_multiple_modules(masses):
    total_fuel = 0
    for mass in masses:
        total_fuel += recursive_fuel_required_single_module(mass)
    return total_fuel


def test_fuel_required_single_module():
    assert fuel_required_single_module(12) == 2
    assert fuel_required_single_module(14) == 2
    assert fuel_required_single_module(1969) == 654
    assert fuel_required_single_module(100756) == 33583


def test_fuel_required_multiple_modules():
    assert fuel_required_multiple_modules([12, 14, 1969, 100756]) == 34241


def test_answer_1():
    with open('input') as f:
        assert fuel_required_multiple_modules([int(line.rstrip('\n')) for line in f]) == 3372695


def test_recursive_fuel_required_single_module():
    assert recursive_fuel_required_single_module(14) == 2
    assert recursive_fuel_required_single_module(1969) == 966
    assert recursive_fuel_required_single_module(100756) == 50346


def test_recursive_fuel_required_multiple_modules():
    assert recursive_fuel_required_multiple_modules([14, 1969, 100756]) == 51314


def test_answer_2():
    with open('input') as f:
        assert recursive_fuel_required_multiple_modules([int(line.rstrip('\n')) for line in f]) == 5056172
