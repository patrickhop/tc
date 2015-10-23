## This is the text editor interface. 
## Anything you type or change here will be seen by the other person in real time.


## [... ("NAME",score) ... ] sorted alphabetically
## score = sum of letter scores * log(position in the the sorted list starting at 1)
## letter scores A:1,..,Z:26
## e.g. "NAME" @ position 100 => N:14,A:1,M:13,E:5 => 33*log(100)

## str = raw_input()

import string
import math

def stringToSubScore(input):
    score = 0
    for i in xrange(0, len(input)):
        score += ord(input[i]) - 64
    return score

# tested parsing
input = raw_input()
input = input.split('\",\"')
input[0] = string.replace(input[0], '\"', '')
input[-1] = string.replace(input[-1], '\"', '')

# input = ['AAB', 'BBB']

indices = []
for i in xrange(1, len(input) + 1):
    indices.append(i)

inputsAndSubScores = map(lambda x: (x, stringToSubScore(x)), sorted(input))
subScoresAndIndices = zip(inputsAndSubScores, indices)
collapsed = map(lambda x: (x[0][0], x[0][1], x[1]), subScoresAndIndices)
scoredNames = map(lambda x: (x[0], x[1]* math.log(x[2])), collapsed)

print scoredNames