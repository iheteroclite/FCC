import sys
import re

def arithmetic_arranger(problems, calculate=False):
    """ Returns up to 5 long addition and subtraction formatted sums,
    with the answers when calculate is True. """

    # Error checking
    if len(problems) > 5:  # More than 5 problems error
        return 'Error: Too many problems.'

    problems_parts = []
    length = []

    for x, problem in enumerate(problems):
        if '+' not in problem and '-' not in problem:  # Isn't + or - sum error
            return "Error: Operator must be '+' or '-'."
        # problem_parts[x][1] = operator and problem[x][0], problem[x][2]= operands
        problems_parts.append(re.split(r"([+-])", problem.replace(' ', '') ))

        if len(problems_parts[x][0]) > len(problems_parts[x][2]):
            length.append(len(problems_parts[x][0]))
        else:
            length.append(len(problems_parts[x][2]))

        if (length[x] > 4):
            return 'Error: Numbers cannot be more than four digits.'

        if not (problems_parts[x][0].isdigit() and problems_parts[x][2].isdigit()):
            return 'Error: Numbers must only contain digits.'

    # Calculation and formatting
    i = 0
    lines = ['']*4
    answer = 0
    for top, sign, bottom in problems_parts:
        # Calculate sum
        if calculate is True:
            if sign == '+':
                answer = int(top) + int(bottom)
            else:
                answer = int(top) - int(bottom)
            lines[3] += (str(answer).rjust(length[i] + 2) + '    ')

        # Format output lines
        lines[0] += (top.rjust(length[i] + 2) + '    ')
        lines[1] += (sign + bottom.rjust(length[i] + 1) + '    ')
        lines[2] += ('-'*(length[i]+2) + '    ')

        i += 1

    # Concatenate lines into str output
    if calculate is True:
        arranged_problems = '\n'.join(line[:-4] for line in lines)
    else:
        arranged_problems = '\n'.join(line[:-4] for line in lines[0:3])
    return arranged_problems