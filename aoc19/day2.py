import os
import intcode

_INPUT_PATH = os.path.join(os.path.dirname(__file__), 'inputs', 'input2.txt')


def part1():
    return intcode.execute_from_disk(_INPUT_PATH, 12, 2)


def part2():
    program = intcode.load(_INPUT_PATH)
    for n in range(100):
        for v in range(100):
            if intcode.execute_from_memory(program, n, v) == 19690720:
                return 100 * n + v
