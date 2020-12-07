import sys
import re

shinyBagList = {}  # dict containing all bags that can directly hold a shiny gold bag
bagList = {}    # dict containing all other bags

with open(sys.path[0] + '/input.txt') as f:
    entry = ''
    for line in f:
        # regex space trims splitted parts and removes " bag.\n OR bags.\n"
        line = re.sub(" bags?[.,]?|\n|contain |no other", '', line)
        bagSpec = re.split("(\\d \\w+ \\w+)", line)
        bagSpec = [i.strip() for i in bagSpec if i.strip()]  # remove empty values
        # print(bagSpec)
        # [1:] returns [] if len(bagspec) ==1
        bagList[bagSpec[0]] = bagSpec[1:]


def countContainedBags(bag):
    bagContent = bagList[bag]
    # print(f"\nThe {bag} bag contains {bagContent}")
    amount = 0
    multiplicand = 0
    result = amount
    for b in bagContent:                    # split and count the contribution of each individual bag
        a, bagName = b.split(' ', 1)
        amount = int(a)
        multiplicand = int(countContainedBags(bagName))
        result += amount + amount * multiplicand
        # print(f"there are {amount} {bagName} bags, each containing another {multiplicand} bags")
    # print(f"the {bag} bag contains a total of {result} bags")
    return result          

print(f"The shiny gold bag contains a total of {countContainedBags('shiny gold')} bags") # check content of shiny gold bag

