import sys

answered_questions = []

def countQuestions(entry):
    tset = set(entry)
    # print(f"\non entry {entry}, {len(tset)} questions were answered")
    # print(tset)
    answered_questions.append(len(tset))


with open(sys.path[0] + '/input.txt') as f:
    entry = ''
    for line in f:
        line = line.strip()
        if(not line and entry):  # empty line found whilst entry contains data
            countQuestions(entry)
            entry = ''  # clear entry
        else:
            entry += line
countQuestions(entry) # last row of the file

print(f"A total of {sum(answered_questions)} were answered")

# CORRECT!