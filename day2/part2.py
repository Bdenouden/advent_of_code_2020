import sys

valid = 0

with open(sys.path[0] + '/input.txt') as f:
    lines = f.readlines()

    for line in lines:
        line = line.strip()

        l = line.split(': ')  # split instruction from content
        instr = l[0]  # instruction e.g. '1-3 c'
        key = instr[-1]  # 'c'
        index = instr[0:-2].split('-')
        iMin = int(index[0])-1
        iMax = int(index[1])-1

        pw = l[1]  # password to be testes

        print(f"\n{line}")
        if((pw[iMin] == key) ^ (pw[iMax] == key)):
            valid += 1
            print("VALID")
        else:
            print("INVALID")


print(f"Valid passwords: {valid}")

# CORRECT!
