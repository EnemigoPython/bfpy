from readchar import readchar
from io import TextIOWrapper
import sys
import re


def parse_file(f: TextIOWrapper):
    instruction_set = r'[><+-.,\[\]]'
    return ''.join(''.join(re.findall(instruction_set, l)) for l in f.readlines())


def execute_instructions(instructions: str):
    instruction_pointer = 0
    data_pointer = 0
    cells = [0]
    open_brackets = list()
    while instruction_pointer < len(instructions):
        current_instruction = instructions[instruction_pointer]
        match current_instruction:
            case '>':
                data_pointer += 1
                if data_pointer == len(cells):
                    cells.append(0)
            case '<':
                if data_pointer == 0:
                    print("Data pointer out of bounds")
                    sys.exit(1)
                data_pointer -= 1
            case '+':
                cells[data_pointer] += 1
            case '-':
                cells[data_pointer] -= 1
            case '.':
                print(chr(cells[data_pointer]), end='')
            case ',':
                cells[data_pointer] = ord(readchar())
            case '[':
                if cells[data_pointer] == 0:
                    try:
                        remaining_closing_brackets = 1
                        while remaining_closing_brackets > 0:
                            instruction_pointer += 1
                            current_instruction = instructions[instruction_pointer]
                            if current_instruction == '[':
                                remaining_closing_brackets += 1
                            if current_instruction == ']':
                                remaining_closing_brackets -= 1
                    except IndexError:
                        print("Unmatched opening bracket")
                        sys.exit(1)
                else:
                    open_brackets.append(instruction_pointer)
            case ']':
                if cells[data_pointer] != 0:
                    instruction_pointer = open_brackets[-1]
                else:
                    open_brackets.pop()
        instruction_pointer += 1


def main():
    if len(sys.argv) <= 1:
        print("brainf*ck interpreter")
        print("usage: bfinterpreter <targetfile>")
        return
    try:
        filename = sys.argv[1]
        with open(filename, 'r') as f:
            instructions = parse_file(f)
            execute_instructions(instructions)
    except Exception as e:
        print(f"Error reading file {filename}")
        print(e)
        return


if __name__ == '__main__':
    main()
