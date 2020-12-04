import sys
totalValidPassports = 0
requiredKeys = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    # "cid"
]


def checkPassPort(data):
    global totalValidPassports
    print("------------")
    print(f"Entry = {entry}")

    keys = []
    for item in entry.split(" "):
        keys.append(item.split(":")[0])

    isValid = all(e in keys for e in requiredKeys)
    if isValid:
        totalValidPassports += 1
    print(f"Keys = {keys}")
    print(f"isValid: {isValid}")
    print("------------")


with open(sys.path[0] + '/input.txt') as f:
    entry = ''
    for line in f:
        line = line.strip()
        print(line, end="->")
        print(bool(line))

        if(not line and entry):
            checkPassPort(entry)
            entry = ''
        else:
            entry += line + " "
    checkPassPort(entry)  # check last rules of the input

print(f"\n\nTotalValidPasswords = {totalValidPassports}")

# CORRECT!