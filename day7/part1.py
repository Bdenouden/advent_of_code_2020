import sys
import re

shinyBagList = {}  # dict containing all bags that can directly hold a shiny gold bag
bagList = {}    # dict containing all other bags

with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        # regex space trims splitted parts and removes " bag.\n OR bags.\n"
        line = re.sub(" bags?.\n", '', line)
        bagSpec = re.split(r" bags contain \d+ | bags?, \d+ ", line)
        # print(bagSpec)
        if("shiny gold" in bagSpec[1:]):
            shinyBagList[bagSpec[0]] = bagSpec[1:]
        elif (len(bagSpec[1:]) >= 1):
            bagList[bagSpec[0]] = bagSpec[1:] # [1:] returns [] if len(bagspec) ==1





runLoop = True
while runLoop:
    lengtBeforeLoop = len(shinyBagList)

    for bag in bagList.copy():
        intersection = bagList[bag] & shinyBagList.keys()
        if(len(intersection) > 0):
            shinyBagList[bag] = bagList[bag]
            del bagList[bag]

    # cycle through loop again if the length changed last loop
    runLoop = lengtBeforeLoop != len(shinyBagList)
    if(runLoop):
        print("The plot thickens!")




print(f"\nA total of {len(shinyBagList)} can eventually hold the shiny gold bag")

# CORRECT!