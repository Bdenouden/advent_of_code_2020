import sys
import re

bagList = {}    # dict containing all bags

with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        line = re.sub(" bags?[.,]?|\n|contain |no other", '', line)
        bagSpec = re.split(r"(\d \w+ \w+)", line)
        bagSpec = [i.strip() for i in bagSpec if i.strip()]  # remove empty values
        bagList[bagSpec[0]] = bagSpec[1:]


def countContainedBags(bag):
    result = 0
    for b in bagList[bag]:                    # split and count the contribution of each individual bag
        a, bagName = b.split(' ', 1)
        amount = int(a)
        multiplicand = int(countContainedBags(bagName))
        result += amount + amount * multiplicand
    return result          

print(f"The shiny gold bag contains a total of {countContainedBags('shiny gold')} bags") # check content of shiny gold bag

# CORRECT!