import sys

answered_questions = []


def countQuestions(entry):
    entry = entry.strip().split("\n")
    baseSet = set(entry[0])
    for i in entry:
        baseSet = baseSet.intersection(i)

    answered_questions.append(len(baseSet))
    # print(f"Entry: {entry} \nresults in length: {len(baseSet)}\n")


with open(sys.path[0] + '/input.txt') as f:
    entry = ''
    for line in f:
        if(line == "\n" and entry):  # empty line found whilst entry contains data
            countQuestions(entry)
            entry = ''  # clear entry
        else:
            entry += line
countQuestions(entry)  # last row of the file

print(f"A total of {sum(answered_questions)} were answered")

# CORRECT!