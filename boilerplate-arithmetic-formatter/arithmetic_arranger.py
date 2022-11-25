import sys
import re

def arithmetic_arranger(problems, calculate=False):
    # Check input params (problems), more than 5 items should error
    if len(problems) > 5:
        return 'Error: Too many problems.'

    problems_parts = []
    length = []

    for x, problem in enumerate(problems):
        # Check input contains a + or -
        if '+' not in problem and '-' not in problem:
            return "Error: Operator must be '+' or '-'."
        # Split on the operand so you have problem[1] = operator and problem[0] and problem[2] being the operands
        problems_parts.append(re.split(r"([+-])", problem.replace(' ', '') ))

        if len(problems_parts[x][0]) > len(problems_parts[x][2]):
            length.append(len(problems_parts[x][0]))
        else:
            length.append(len(problems_parts[x][2]))

        if (length[x] > 4):
            #sys.exit('Error: Numbers cannot be more than four digits.')
            return 'Error: Numbers cannot be more than four digits.'

# check longest
    #first_longer = []
    # # use rjust()
    i = 0
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''
    answer = 0
    for top, sign, bottom in problems_parts:
        if calculate is True:
            if sign == '+':
                answer = int(top) + int(bottom)
            else:
                answer = int(top) - int(bottom)
            line4 += (str(answer).rjust(length[i] + 2) + '    ')

        line1 += (top.rjust(length[i] + 2) + '    ')
        line2 += (sign + bottom.rjust(length[i] + 1) + '    ')
        line3 += ('-'*(length[i]+2) + '    ')

        i += 1
        # TODO make lines list, and use join to join with \n
    if calculate is True:
        arranged_problems = line1[:-4] + '\n' + line2[:-4] + '\n' + line3[:-4] + '\n' + line4[:-4]
    else:
        arranged_problems = line1[:-4] + '\n' + line2[:-4] + '\n' + line3[:-4]

    return arranged_problems