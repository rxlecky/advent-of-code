def execute_from_disk(path: str, a: int, b: int) -> int:
    program = load(path)
    program[1] = a
    program[2] = b
    return _execute_from_memory(program)


def execute_from_memory(program: [int], a: int, b: int) -> int:
    program_copy = program.copy()
    program_copy[1] = a
    program_copy[2] = b
    return _execute_from_memory(program_copy)


def load(path: str) -> [[int]]:
    with open(path) as file:
        return [int(code) for code in file.read().split(',')]


def _fetch_instruction(pointer: int, memory: [int]) -> (int,):
    if memory[pointer] == 99:
        return 99, -1, -1, -1
    return tuple(memory[pointer + i] for i in range(4))


def _decode_instruction(instruction: int):
    opcodes = {
        1: lambda a, b: a + b,
        2: lambda a, b: a * b,
        99: lambda a, b: -1
    }
    return opcodes[instruction]


def _execute_instruction(instruction: (int,), memory: [int]) -> None:
    (o, a, b, d) = instruction
    if o == 99:
        return
    memory[d] = _decode_instruction(o)(memory[a], memory[b])


def _execute_from_memory(program: [int]) -> int:
    instruction = _fetch_instruction(0, program)
    i = 4
    while instruction[0] != 99:
        _execute_instruction(instruction, program)
        instruction = _fetch_instruction(i, program)
        i += 4
    return program[0]
