import sys


def getInstructions(target):
    instructions = []
    target_count = 0
    with open(sys.path[0] + '/input.txt') as f:
        for line in f:
            ins, num = line.split(' ')
            instructions.append({'i': ins, 'num': int(num)})
            if(ins == target):
                target_count += 1
    return instructions, target_count


def runProgram(instructions):
    acc = 0
    visitedLines = []
    nextLine = 0
    while nextLine not in visitedLines and nextLine < len(instructions):
        visitedLines.append(nextLine)
        inst = instructions[nextLine]
        if(inst['i'] == 'acc'):
            acc += inst['num']
            nextLine += 1
        elif(inst['i'] == 'jmp'):
            nextLine += inst['num']
        else:
            nextLine += 1
    return acc, nextLine == len(instructions)


def changeXToY(inst, jmpNum, X, Y):
    count = 0
    for i in inst:
        if i['i'] == X:
            if(count == jmpNum):
                i['i'] = Y
                break
            count += 1
    return inst


isEOF = False # end of file reached?
iter = 0 # iterator for the instruction to change

X = 'jmp'   # instruction to replace
Y = 'nop'   # replacement for instruction

while not isEOF:
    original_instructions, target_count = getInstructions('jmp')
    instructions = changeXToY(original_instructions, iter, X, Y)
    acc, isEOF = runProgram(instructions)

    if(iter == target_count - 1):
        break
    else:
        iter += 1

print(f"\nAcc = {acc}, is this a solution: {isEOF}\n")

# CORRECT!