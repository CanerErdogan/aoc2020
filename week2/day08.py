from copy import deepcopy

class Instruction:
    def __init__(self, operation, argument):
        self.opr = operation
        self.arg = int(argument)
        self.executed = False

    
    def __call__(self, order, accumulator):
        self.executed = True
        if self.opr == 'acc':
            return [order + 1, accumulator + self.arg]
        elif self.opr == 'jmp':
            return [order + self.arg, accumulator]
        return [order + 1, accumulator]

    
    def __repr__(self):
        return f"{self.opr} {self.arg}"

    
    def switch(self):
        self.opr = 'jmp' if self.opr == 'nop' else 'nop'
        return self


with open('day08.txt') as fp:
    batch = fp.read().strip().split('\n')
    instructions = []
    for line in batch:
        operation, argument = line.split()
        instructions.append(Instruction(operation, argument))


def single_execution(instructions):
    accumulator = order = 0
    instructions = deepcopy(instructions)
    while True:
        if instructions[order].executed:
            return accumulator
        order, accumulator = instructions[order](order, accumulator)


def fix_program(instructions):
    attempt = 0
    while True:
        accumulator = order = 0
        fixed_instructions = deepcopy(instructions)
        while fixed_instructions[attempt].opr == 'acc':
            attempt += 1
        fixed_instructions[attempt].switch()
        while True:
            if fixed_instructions[order].executed:
                break
            order, accumulator = fixed_instructions[order](order, accumulator)
            if order == len(fixed_instructions):
                return accumulator
        attempt += 1
        


print("Before any second execution: ", single_execution(instructions))
print("Accumulator after termination: ", fix_program(instructions))
