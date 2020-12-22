import sys


f = open(sys.path[0] + '/input.txt').read().split("\n\n")
p1 = [int(num.strip()) for num in f[0].split("\n")[1:]]
p2 = [int(num.strip()) for num in f[1].split("\n")[1:]]     

def updateHands(winner, loser):
    wCard, lCard = winner[0], loser[0]
    loser = loser[1:] # remove card from loser hand
    winner = winner[1:] # place cards in winner hand
    winner.extend([wCard, lCard])

    return winner, loser

def getScore(p):
    maxPoints = len(p)
    score = 0
    for i, num in enumerate(p):
        score += (maxPoints-i)*num
    return score

round = 1
while p1 and p2: # play until a hand is empty
    if p1[0] > p2[0]: # player 1 wins
        p1, p2 = updateHands(p1, p2)
    elif p2[0] > p1[0]: # player 2 wins
        p2, p1 = updateHands(p2,p1)
    else:
        exit(f"ERROR: p1: {p1[0]}, p2: {p2[0]}")
    round += 1
print("Game end!")
print(f"\n--- P1 --- \nDeck: {p1}\nScore: {getScore(p1)}")
print(f"\n--- P2 --- \nDeck: {p2}\nScore: {getScore(p2)}")

# CORRECT!