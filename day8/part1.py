import sys

acc = 0
instructions = []

with open(sys.path[0] + '/input.txt') as f:
    for line in f:
        ins, num = line.split(' ')
        instructions.append({'i': ins, 'num': int(num)})

visitedLines = []
nextLine = 0

while nextLine not in visitedLines:
    visitedLines.append(nextLine)
    inst = instructions[nextLine]

    if(inst['i'] == 'acc'): 
        acc += inst['num']
        nextLine += 1
    elif(inst['i'] == 'jmp'):
        nextLine += inst['num']
    else:
        nextLine += 1
    
print(f"Acc = {acc}")

# CORRECT!