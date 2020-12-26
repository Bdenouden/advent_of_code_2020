import sys


def getLoopSize(pk):
    val = 1
    subNum = 7
    i = 1
    while True:
        val = (val * subNum) % 20201227
        if val == pk:
            print(f"loopSize = {i}")
            break
        i += 1
    return i

def transform(subNum, loopSize):
    val = 1
    for _ in range(loopSize):
        val = (val * subNum) % 20201227
    return val

with open(sys.path[0] + '/input.txt') as f:
    nums = f.read().split("\n")
    pk_card = int(nums[0])
    pk_door = int(nums[1])

loopSize1 = getLoopSize(pk_card)
print(transform(pk_door, loopSize1))

loopSize2 = getLoopSize(pk_door)
print(transform(pk_card, loopSize2))

# CORRECT!