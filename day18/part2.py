import sys
import re


def performAction(num1, action, num2):
    if action == '*':
        return num1 * num2
    elif action == '+':
        return num1 + num2

    exit(f"Oops!...\n n1: {num1}, action: {action}, n2: {num2}")


def stripParentheses(string):
    openBr = 1
    subcalc = ''
    for c in string:
        if c == '(':
            openBr += 1
        elif c == ')':
            openBr -= 1

        if openBr == 0:
            break
        subcalc += c
    parRes = doMath(subcalc)

    return subcalc, str(parRes)


def doMath(string):
    substr = ''
    res = None
    action = None

    parPos = string.find('(')
    while parPos != -1:
        old, new = stripParentheses(string[parPos+1:])
        string = string.replace(f"({old})", new)
        parPos = string.find('(')

    for c in string:
        if c == '*' or c == '+':
            if action is not None:
                res = performAction(res, action, int(substr))
            else:
                res = int(substr)
            action = c
            substr = ''
        else:
            substr += c
    # perform last operation
    res = performAction(res, action, int(substr))
    return res


def addPriority(string):
    match = re.findall(r"((?:\d+\+)+\d+)", string)
    falseMatch = re.findall(r"\(((?:\d+\+)+\d+)\)", string)
    match = list(set(match) - set(falseMatch))
    for m in match:
        if m == string:
            return string
        string = string.replace(f"{m}", f"({m})")
    return string


def getPars(string):
    match = re.findall(r"\(([^()]+)\)", string)
    for m in match:
        calc = addPriority(m)
        calc = doMath(calc)
        string = string.replace(f"({m})", str(calc))
    if '(' in string:
        string = getPars(string)
    return string


results = []
with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        mathString = line.strip().replace(' ', '')
        # print(f"\nIn: {mathString}")
        # print(mathString)
        mathString = getPars(mathString)
        mathString = addPriority(mathString)
        result = doMath(mathString)
        # print(f"Out: {result}")

        results.append(result)

print(f"solution: {sum(results)}")
