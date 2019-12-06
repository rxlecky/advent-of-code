import os


def part1():
    return _compute_total_consumption(_compute_consumption_without_fuel)


def part2():
    return _compute_total_consumption(_compute_consumption_with_fuel)


_INPUT_PATH = os.path.join(os.path.dirname(__file__), 'inputs', 'input1.txt')


def _parse_input() -> [int]:
    with open(_INPUT_PATH) as file:
        return [int(mass) for mass in file]


def _compute_consumption_without_fuel(mass: int) -> int:
    return (mass // 3) - 2


def _compute_consumption_with_fuel(mass: int) -> int:
    consumption = _compute_consumption_without_fuel(mass)
    if consumption > 0:
        return consumption + _compute_consumption_with_fuel(consumption)
    return 0


def _compute_total_consumption(computation_method):
    module_masses = _parse_input()
    return sum(computation_method(module_mass) for module_mass in module_masses)
