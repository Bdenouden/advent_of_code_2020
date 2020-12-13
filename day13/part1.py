import sys
import re

with open(sys.path[0] + '/input.txt') as f:
    lines = f.read().splitlines()

TOA = int(lines[0])
busIds = [int(id) for id in re.findall(r"(\d+)", lines[1])]


closest = {}
for id in busIds:
    delta = id - TOA % id
    if not closest or delta < closest['time'] :
        closest['time'] = delta
        closest['id'] = id

print(f"Your answer = {closest['time'] * closest['id']}")

# CORRECT!       