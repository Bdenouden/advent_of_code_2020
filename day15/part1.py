import sys

with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        numbers = [int(num) for num in line.strip().split(',')]

turn = len(numbers)  # index of the turn (actual turn is 1 larger)
lastOccurence = {num: i for i, num in enumerate(numbers)}
while True:
    lastSpoken = numbers[-1]
    if(numbers.count(lastSpoken) == 1):
        numbers.append(0)
    elif (numbers[-2] == lastSpoken):
        numbers.append(1)
    else:
        index = lastOccurence[lastSpoken]
        newVal = turn - 1 - index
        numbers.append(newVal)

    lastOccurence[numbers[-2]] = turn - 1
    if turn >= 2019:
        print(f"Solution: {numbers[-1]}")
        exit('Reached last turn!')

    turn = len(numbers)

# CORRECT!