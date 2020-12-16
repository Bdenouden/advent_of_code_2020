import sys
import re

reading = 1
rules = {}


valid = set()
invalid = []


def getRule(line):
    ruleName, param = line.split(':')
    values = [int(val) for val in re.findall(r"(\d+)", param)]
    rules[ruleName] = values
    return values


def getYourTicket(line):
    pass


def getOtherTicket(line):
    return [int(num) for num in re.findall(r"(\d+)", line)]


def setBounds(r):
    """
    argument: `list` of 4 values
    `[lower bound 1, upper bound 1, lower bound 2, upper bound 2]`
    """
    global valid

    for i in range(r[0], r[1]+1):
        valid.add(i)

    for i in range(r[2], r[3]+1):
        valid.add(i)


def checkTicket(t):
    for num in t:
        if num not in valid:
            invalid.append(num)


with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        if line == "\n":  # empty line found, skip to next part
            reading += 1
        elif reading == 1:
            value = getRule(line.strip())
            setBounds(value)
        elif reading == 2:
            getYourTicket(line.strip())
        elif reading == 3:
            ticket = getOtherTicket(line.strip())
            checkTicket(ticket)
        else:
            exit('this was not supposed to happen....')

print(f"\nInvalid: {invalid}, sum = {sum(invalid)}")

# CORRECT!
