import sys


cupList = [int(num) for num in open(sys.path[0] + '/input.txt').read().strip()]
cupList.extend([i for i in range(len(cupList)+1, int(1e6)+1)])  # start at value 10, end at value 1e6

cups = {cup: (cupList[i+1] if i < len(cupList)-1 else cupList[0]) # create linked list in dict
        for i, cup in enumerate(cupList)}      

print("Start Crab Cups!")

curCup = cupList[0]         # initial value of current cup
for i in range(int(1e7)+1): # Number of iterations
    
    # get 3 cups
    a = cups[curCup]
    b = cups[a]
    c = cups[b]

    # bypass those cups in the list (excluding them)
    cups[curCup] = cups[c]

    # get destination cup
    destCup = curCup-1  
    while True:
        if destCup > 0 and destCup not in [a,b,c]:
            break
        destCup -= 1
        if destCup < 1:
            destCup = max(cups.keys())

    # place 3 selected cups back
    cups[c] = cups[destCup]
    cups[destCup] = a

    curCup = cups[curCup]  # set curcup for next iteration

s1 = cups[1]
s2 = cups[s1]

print(f"Solution: {s1} * {s2} = {s1*s2}")

# CORRECT!
