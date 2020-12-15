import sys

with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        numbers = [int(num) for num in line.strip().split(',')]

turn = len(numbers)  # index of the turn (actual turn is 1 larger)
lastOccurence = {num: i for i, num in enumerate(numbers)}

numbers = numbers[-2:]
while True:
    lastSpoken = numbers[-1]
    lastOccured = lastOccurence.get(lastSpoken, None)

    if numbers[-1] == numbers[-2]:
        # last two numbers were equal
        numbers.append(1)
    elif(lastOccured is None or lastOccured == turn-1):  # first encounter
        # write current turn with value 0 to notInDict
        numbers.append(0)
    else:
        numbers.append(turn - lastOccured - 1)

    lastOccurence[numbers[-2]] = turn - 1
    numbers = numbers[-2:]  # decrease buffer

    if turn % 10000 == 0:
        print(turn)

    if turn >= 30000000 - 1:
        print(f"\nSolution: {numbers[-1]}")
        exit('Reached last turn!')

    turn += 1

# CORRECT!