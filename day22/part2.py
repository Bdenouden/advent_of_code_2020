import sys


def updateHands(winner, loser):
    wCard, lCard = winner[0], loser[0]
    loser = loser[1:]  # remove card from loser hand
    winner = winner[1:]  # place cards in winner hand
    winner.extend([wCard, lCard])

    return winner, loser


def getScore(p):
    maxPoints = len(p)
    score = 0
    for i, num in enumerate(p):
        score += (maxPoints-i)*num
    return score


def playRecCombat(p1, p2, game=1):
    print(f"\n== Game {game} ===")

    log = []  # log of previous hands
    round = 1
    while p1 and p2:  # play until a hand is empty
        print(f"\n-- Round {round} (Game {game}) --")
        print(f"Player 1's deck: {p1}")
        print(f"Player 2's deck: {p2}")
        print(f"Player 1 plays: {p1[0]}")
        print(f"Player 2 plays: {p2[0]}")

        # Check if this game config has been achieved earlier
        if {'p1': p1, 'p2': p2} in log[:-1]:
            return p1, []  # player 1 wins this game

        elif p1[0] <= len(p1[1:]) and p2[0] <= len(p2[1:]):
            print("Playing a sub-game to determine the winner...")
            deck1 = p1[1:1+p1[0]]
            deck2 = p2[1:1+p2[0]]
            sp1, sp2 = playRecCombat(deck1, deck2, game=game + 1)

            print(f"...anyway, back to game {game}.")
            if(len(sp1) > len(sp2)):   # winner has largest deck, True if p1 won the game
                p1, p2 = updateHands(p1, p2)
                print(f"Player 1 wins round {round} of game {game}!")
            else:
                p2, p1 = updateHands(p2, p1)
                print(f"Player 2 wins round {round} of game {game}!")
        elif p1[0] > p2[0]:  # player 1 wins
            p1, p2 = updateHands(p1, p2)
            print(f"Player 1 wins round {round} of game {game}!")
        elif p2[0] > p1[0]:  # player 2 wins
            p2, p1 = updateHands(p2, p1)
            print(f"Player 2 wins round {round} of game {game}!")
        else:
            exit(f"ERROR: p1: {p1[0]}, p2: {p2[0]}")

        log.append({'p1': p1, 'p2': p2})  # append to log
        round += 1
    return p1, p2


f = open(sys.path[0] + '/input.txt').read().split("\n\n")
p1 = [int(num.strip()) for num in f[0].split("\n")[1:]]
p2 = [int(num.strip()) for num in f[1].split("\n")[1:]]

p1, p2 = playRecCombat(p1, p2)
print("Game end!")
print(f"\n--- P1 --- \nDeck: {p1}\nScore: {getScore(p1)}")
print(f"\n--- P2 --- \nDeck: {p2}\nScore: {getScore(p2)}")

# CORRECT!
