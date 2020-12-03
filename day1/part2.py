import sys

num = []

with open(sys.path[0] + '/input.txt') as f:
    lines = f.readlines()

    for line in lines:
        line.strip()
        num.append(int(line))

for i in num:
    for j in num: 
        for k in num:
            if i+j+k == 2020:
                print(f"{i}+{j}+{k} == 2020")
                print(f"Answer: {i*j*k}")
                exit()

# CORRECT!