import sys
import re

reading = 1
rules = {}

valid = set()
ticketColumns = {}

def getRule(line):
    ruleName, param = line.split(':')
    values = [int(val) for val in re.findall(r"(\d+)", param)]
    rules[ruleName] = [
        set(range(values[0], values[1] + 1)),
        set(range(values[2], values[3] + 1))
    ]
    return values


def getMyTicket(line):
    return [int(num) for num in re.findall(r"(\d+)", line)]


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
    if not t:
        return False

    for num in t:
        if num not in valid:
            return False
    return True


with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        if line == "\n":  # empty line found, skip to next part
            reading += 1
        elif reading == 1:
            value = getRule(line.strip())
            setBounds(value)
        elif reading == 2:
            myTicket = getMyTicket(line.strip())
        elif reading == 3:
            ticket = getOtherTicket(line.strip())
            if(checkTicket(ticket)):
                for i, val in enumerate(ticket):
                    ticketColumns.setdefault(i, []).append(val)
        else:
            exit('this was not supposed to happen....')


def checkRule(vals):
    name_options = []
    for name in list(rules.keys()):
        for i, val in enumerate(vals):
            if val not in rules[name][0] and val not in rules[name][1]:
                # wrong column name
                break
            if(i == len(vals)-1):
                name_options.append(name)
    return name_options


# get all valid fieldName options for each column
name_options = {}
for colNo, vals in ticketColumns.items():
    name_options[colNo] = checkRule(vals)


# Match columns with a unique fieldName
sorted_names = sorted(name_options, key=lambda k: len(name_options[k]))
col_name_link = {sorted_names[0]: name_options[sorted_names[0]][0]}
for i, key in enumerate(sorted_names[1:]):
    fieldName = [n for n in name_options[sorted_names[i+1]]
                 if n not in name_options[sorted_names[i]]][0]
    col_name_link[key] = fieldName

# Decipher my ticket
myMatchedTicket = {col_name_link[i]: val for i, val in enumerate(myTicket)}
print("\nMy translated ticket:")
[print(key, ':', value) for key, value in myMatchedTicket.items()]
solution_keys = [key for key in list(
    myMatchedTicket.keys()) if re.findall(r"departure", key)]

# Solve puzzle
print("\nFields required for solution:")
mult = 1
for key in solution_keys:
    print(key, '->', myMatchedTicket[key])
    mult *= myMatchedTicket[key]

print(f"\nSolution = {mult}")

# CORRECT!