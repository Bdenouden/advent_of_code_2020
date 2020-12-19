import sys
import re

rules = dict()
messages = list()
readRules = True

with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        if(line == "\n"):
            readRules = False
        elif readRules:
            num, rule = line.strip().split(': ')
            rules[int(num)] = rule
        else:
            messages.append(line.strip())
rules[8] = "42 | 42 8"
rules[11] = "42 31 | 42 11 31"


def getRule(ruleNum, depth = 0):
    rule = rules[ruleNum]
    if ruleNum == 8:
        return '(?:'+getRule(42)+')+'
    elif ruleNum == 11:
        if depth <= 10:
            return f"(?:{getRule(42)}{getRule(11, depth = depth + 1)}?{getRule(31)})"
        else:
            return f"(?:{getRule(42)}{getRule(31)})"

    # if this rule specifies a or b, return this!
    letterMatch = re.findall(r"[ab]", rule)
    if letterMatch:
        return letterMatch[0]

    # determine if or statement is applicable
    rule = rule.split('|')

    pattern = ['']*len(rule)
    for i, r in enumerate(rule):
        # this rule points to other rules
        rulePointer = re.findall(r"\d+", r)

        for num in rulePointer:
                pattern[i] += getRule(int(num))

    return '(?:' + '|'.join(pattern) + ')'


pattern = getRule(0) + '$'

exp = re.compile(pattern)
valid = list(filter(exp.match, messages))

print(f"Pattern = {pattern}, \nvalid: {len(valid)}")

# CORRECT!