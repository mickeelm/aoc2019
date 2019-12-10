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
