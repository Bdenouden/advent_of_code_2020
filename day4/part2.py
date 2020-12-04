import sys
totalValidPassports = 0
totalHasRequiredKeys = 0
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

rules = {
    "byr": {
        "type": int,
        "intBase": 10,
        "length": 4,
        "default":
        {
            "minVal": 1920,
            "maxVal": 2002
        }
    },
    "iyr": {
        "type": int,
        "intBase": 10,
        "length": 4,
        "default":
        {
            "minVal": 2010,
            "maxVal": 2020
        }
    },
    "eyr": {
        "type": int,
        "intBase": 10,
        "length": 4,
        "default":
        {
            "minVal": 2020,
            "maxVal": 2030
        }
    },
    "hgt": {
        "type": int,
        "intBase": 10,
        "suffix": ["cm", "in"],
        "cm": {
            "minVal": 150,
            "maxVal": 193,
        },
        "in": {
            "minVal": 59,
            "maxVal": 76
        }
    },
    "hcl": {
        "type": int,
        "intBase": 16,
        "length": 6,
        "prefix": "#",
    },
    "ecl": {
        "type": str,
        "value": [
            "amb",
            "blu",
            "brn",
            "gry",
            "grn",
            "hzl",
            "oth"
        ]
    },
    "pid": {
        "type": int,
        "intBase": 10,
        "length": 9,
    },
}


def checkAttribute(attr, value):
    isValid = True
    suffix = 'default'

    # no rules specied, everything is valid
    if attr not in rules.keys():
        return True

    # get suffix
    # suffix assumed to be 2 char long
    if rules[attr].get('suffix', False):
        if(value[-2:] in rules[attr]['suffix']):
            suffix = value[-2:]
            value = value[:-2]
        else:
            isValid = False

    # get prefix
    if rules[attr].get('prefix', False):  # prefix assumed to be 1 char long
        value = value[1:]

    # verify length including trailing 0
    if rules[attr].get('length', False):
        isValid *= len(str(value)) == rules[attr]['length']

    # convert to required type
    if(rules[attr]['type'] == int):
        try:
            value = int(value, rules[attr].get("intBase", 10))
        except:
            isValid = False

    # check min/max value
    if(
        rules[attr].get(suffix, False)
        and rules[attr][suffix].get('minVal', False)
        and rules[attr][suffix].get('maxVal', False)
    ):
        isValid *= rules[attr][suffix]['minVal'] <= value <= rules[attr][suffix]['maxVal']

    # check if value is in list
    if rules[attr].get('value', False):
        isValid *= value in rules[attr]['value']
    print(f"{attr} : {value} : {suffix} ->\t { 'valid!' if isValid else 'invalid'}")
    return isValid


def checkPassPort(data):
    global totalValidPassports, totalHasRequiredKeys
    print("------------")
    print(f"Entry = {entry}")

    data = {}

    for item in entry.split(" "):
        splitItem = item.split(":")
        if splitItem[0]:  # exclude trailing spaces
            data[splitItem[0]] = splitItem[1]

    hasRequiredAttributes = all(e in data.keys() for e in requiredKeys)

    isValid = False
    if hasRequiredAttributes:
        totalHasRequiredKeys += 1
        isValid = True
        for attr in data:
            isValid *= checkAttribute(attr, data[attr])

        if isValid:
            totalValidPassports += 1

    print(f"Keys = {data.keys()}")
    print(f"hasRequiredAttributes: {hasRequiredAttributes}")
    print(f"isValid: {isValid}")
    print("------------")


with open(sys.path[0] + '/input.txt') as f:
    entry = ''
    for line in f:
        line = line.strip()

        if(not line and entry):
            checkPassPort(entry)
            entry = ''
        else:
            entry += line + " "
    checkPassPort(entry)  # check last rules of the input

print(f"\n\nTotalValidPasswords = {totalValidPassports}")

# CORRECT!
