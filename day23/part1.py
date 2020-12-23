import sys

cups = [int(num) for num in open(sys.path[0] + '/input.txt').read().strip()]


def getDestCup(cups, invalid, val):
    invalid = tuple(invalid)
    while True:
        if val < min(cups):         # wrap val around if to low
            val = max(cups)
        if val not in invalid:    # skip search if val cannot be found
            for i, c in enumerate(cups):
                if c == val:
                    return i, c
        val -= 1                    # subtract 1 from value if the cup is not found


def getCurCup(cups, prevCurCup):
    for i, c in enumerate(cups):
        if c == prevCurCup:
            index = (i+1) % len(cups)
            return index, cups[index]


def pickCups(cups, start):
    pickedCups = []
    newCups = cups.copy()
    for i in range(start, start+3):
        pos = i % len(cups)
        pickedCups.append(cups[pos])
        newCups.remove(cups[pos])
    return newCups, pickedCups


curCup = None
for i in range(100):                 # Number of iterations
    # print(f"\n-- move {i+1} --")
    # print(f"cups: {cups}")
    if curCup is not None:
        curIndex, curCup = getCurCup(cups, curCup)    # Select current cup
    else:
        curIndex, curCup = 0, cups[0]
    # print(f"selected cup: {curCup}")

    cups, pickedCups = pickCups(cups, curIndex+1)      # pick cups
    # print(f"pick up: {pickedCups}")

    destIndex, destCup = getDestCup(cups, pickedCups, curCup - 1)
    # print(f"destination: {destCup}")

    for j in range(3):
        j = j % len(cups)
        cups.insert(destIndex+1+j, pickedCups[j])

print(cups)

# CORRECT!