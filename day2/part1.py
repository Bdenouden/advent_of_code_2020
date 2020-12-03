import sys

valid = 0

with open(sys.path[0] + '/input.txt') as f:
    lines = f.readlines()

    for line in lines:
        line.strip()

        l = line.split(': ')  # split instruction from content
        instr = l[0]  # instruction e.g. '1-3 c'
        key = instr[-1]  # 'c'
        count = instr[0:-2].split('-')
        countMin = int(count[0])
        countMax = int(count[1])

        pw = l[1]  # password to be testes

        count = 0
        for c in pw:
            if c == key:
                count += 1

        print(f"\nmin: {countMin}, max: {countMax}, count: {count}")
        if count >= countMin and count <= countMax:
            valid+=1
            print("VALID")
        else:
            print("INVALID")

print(f"Valid passwords: {valid}")

# CORRECT!