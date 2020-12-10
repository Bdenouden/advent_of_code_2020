#!ptyhon3
import os
import fnmatch
import sys
import re

# get folrders on current path and sort them
folders = fnmatch.filter(os.listdir(sys.path[0]), 'day*')
folders.sort(key=lambda folders: int(re.split(r'(\d+)', folders)[1]))

# set path for new day
currentDay = re.split(r'(\d+)', folders[-1])[:2]
dayNum = int(currentDay[1]) + 1
path = f"{sys.path[0]}\\{currentDay[0]}{dayNum}\\"

# create path and files for new day
files = ['part1.py', 'part2.py', 'input.txt', 'test.txt']
pyFile = [f for f in files if re.search(".py", f)]
try:
    os.makedirs(path)
    print(f"\033[92m{path} created!\033[0m")
except: 
    exit(f"\033[93m{path} already exists!\033[0m")

for file in files:
    f = open(path + file, 'w')
    if file in pyFile:
        f.write("""import sys

with open(sys.path[0] + '/test.txt') as f:
    for line in f:

        """)
    f.close()
    print(f"\033[92m\t- {file} created!\033[0m")