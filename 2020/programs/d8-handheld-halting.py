from os.path import abspath
from itertools import chain


def execute(program):
    
    def destroy_command_after_call(func):
        def wrapper(x):
            nonlocal pointer, repl_program
            init_pointer = pointer
            func(x)
            repl_program[init_pointer] = ("brk", 0)
        return wrapper

    @destroy_command_after_call
    def acc(x):
        nonlocal accumulator
        accumulator += x
    
    @destroy_command_after_call
    def jmp(x):
        nonlocal pointer
        pointer += x - 1

    @destroy_command_after_call
    def nop(x):
        pass

    def brk(x):
        return True
    
    pointer = 0
    accumulator = 0
    repl_program = program.copy()
    while not eval(f"{repl_program[pointer][0]}(int({repl_program[pointer][1]}))"):
        pointer += 1
    return pointer, accumulator
    
def swap_command():
    global program
    exp_program = list(chain.from_iterable(program))
    index = 0
    while True:
        try:
            index = min(exp_program.index("nop", index),
                        exp_program.index("jmp", index))
        except ValueError:
            try:
                index = exp_program.index("nop", index)
            except ValueError:
                index = exp_program.index("jmp", index)
        program[index // 2] = ("jmp" if program[index // 2][0] == "nop" else "nop", program[index // 2][1])
        yield
        program[index // 2] = ("jmp" if program[index // 2][0] == "nop" else "nop", program[index // 2][1])
        index += 2

    
with open(abspath(r".\2020\input\d8-handheld-halting.txt")) as inpf:
    program = [tuple(i.split()) for i in inpf]
    
    print(execute(program)[1])
    
    program.append(("brk", 0))
    swapper = swap_command()
    while execute(program)[0] + 1 < len(program):
        next(swapper)
    print(execute(program)[1])