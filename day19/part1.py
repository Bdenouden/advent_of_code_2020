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


def getRule(ruleNum):
    rule = rules[ruleNum]

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