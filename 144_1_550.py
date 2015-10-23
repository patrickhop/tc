# SRM 144
# DIV 1
# 550

import math

class Lottery:
    def getTupleKey(self, tuple):
        return tuple[1]

    def shiftCounts(self, counts):
        newCounts = list(counts)
        newCounts.insert(0,0)
        return newCounts[0:-1]

    # effectively the same as vector addition
    def sumCounts(self, countsOne, countsTwo):
        #  we want to be able to sum trees of different sizes
        newCounts = []
        maxIndex = max(len(countsOne), len(countsTwo))
        for i in xrange(0, maxIndex):
            a = 0
            b = 0
            if i > len(countsOne) - 1:
                a = 0
                b = countsTwo[i]
            elif i > len(countsTwo) - 1:
                a = countsOne[i]
                b = 0
            else:
                a = countsOne[i]
                b = countsTwo[i]
                newCounts.append(a + b)

        return newCounts

    def computeNotUniqueNotAsc(self, depth, minint, maxint):
        # (maxint-minint)^(depth)
        return int(math.pow((maxint - minint) + 1, depth))

    def computeUniqueNotAsc(self, depth, minint, maxint):
        # maxint! / (maxint - depth)!
        return int(float(math.factorial(maxint - minint + 1)) / float(math.factorial((maxint - minint + 1) - depth)))

    def computeNotUniqueAsc(self, depth, minint, maxint):
        # we might need to compute a new maxint?
        DEPTH = depth
        MAXINT = maxint
        MININT = minint

        # init our lookup table for tree level counts
        counts = {}
        counts[str(MAXINT)] = [1 for x in range(2*DEPTH)]

        for i in xrange(MAXINT - 1, MININT - 1, -1): # shift bounds
            counts[str(i)] = list(counts[str(i + 1)])
            shiftedPriorCounts = list(counts[str(i + 1)])
            for j in xrange(0, DEPTH - 1):
                # shift prior, add to prior
                shiftedPriorCounts = self.shiftCounts(shiftedPriorCounts)
                counts[str(i)] = self.sumCounts(counts[str(i)], shiftedPriorCounts)

        # print counts
        leaves = map(lambda x: counts[x][DEPTH - 1], counts.keys())
        return reduce(lambda x,y: x + y, leaves)



    def computeUniqueAsc(self, depth, minint, maxint):
        # we might need to compute a new maxint?
        DEPTH = depth
        MAXINT = maxint
        MININT = minint

        # init our lookup table for tree level counts
        counts = {}
        counts[str(MAXINT + 1)] = [0 for x in range(2*DEPTH)]
        counts[str(MAXINT + 1)][0] = 0
        counts[str(MAXINT)] = [0 for x in range(2*DEPTH)]
        counts[str(MAXINT)][0] = 1

        # add notion of MININT
        for i in xrange(MAXINT - 1, MININT - 1, -1): # shift bounds
            sum = [0 for x in range(2*DEPTH)]

            upperBound = MAXINT + 1
            lowerBound = i
            for j in xrange(upperBound, lowerBound, -1):
                # print j
                sum = self.sumCounts(sum, counts[str(j)])

            shiftedCounts = self.shiftCounts(sum)
            shiftedCounts[0] = 1
            counts[str(i)] = shiftedCounts
            # print counts

        leaves = map(lambda x: counts[x][DEPTH - 1], counts.keys())
        return reduce(lambda x,y: x + y, leaves)

    def route_and_solve(self, params):
        minint = 1 # hardcoded problem constraint
        maxint = int(params[0])
        depth = int(params[1])
        isSorted = params[2] == 'T'
        isUnique = params[3] == 'T'

        # map params to logic

        sol = -1
        if isSorted == True and isUnique == True:
            sol = lottery.computeUniqueAsc(depth, minint, maxint)
        elif isSorted == True and isUnique == False:
            sol = lottery.computeNotUniqueAsc(depth, minint, maxint)
        elif isSorted == False and isUnique == True:
            sol = lottery.computeUniqueNotAsc(depth, minint, maxint)
        elif isSorted == False and isUnique == False:
            sol = lottery.computeNotUniqueNotAsc(depth, minint, maxint)
        else:
            print 'bad params'
        
        return sol

    def parse_params(self, _input):
        cleaved = map(lambda x: x.split(':'), list(_input))
        dirtyParams = map(lambda x: (x[0], x[1]), cleaved)
        lotteriesAndParams = map(lambda x: (x[0],x[1].split(' ')[1:]), dirtyParams)

        return lotteriesAndParams

    def order(self, tuples):
        tuples = sorted(tuples, key=self.getTupleKey)
        for i in xrange(0, len(tuples) - 1):
            # handle edge case of equal probabilities
            if (tuples[i][1] == tuples[i+1][1]) and (ord(tuples[i][0][0]) > ord(tuples[i+1][0][0])):
                placeholder = tuples[i]
                tuples[i] = tuples[i+1]
                tuples[i+1] = placeholder

        return tuples

# run through topcoder test examples
testCaseOne = {'PICK ANY TWO: 10 2 F F', 'PICK TWO IN ORDER: 10 2 T F',
               'PICK TWO DIFFERENT: 10 2 F T', 'PICK TWO LIMITED: 10 2 T T'} 

testCaseTwo = {'INDIGO: 93 8 T F',
               'ORANGE: 29 8 F T',
               'VIOLET: 76 6 F F',
               'BLUE: 100 8 T T',
               'RED: 99 8 T T',
               'GREEN: 78 6 F T',
               'YELLOW: 75 6 F F'}

testCaseThree = {}

lottery = Lottery()

paramsOne = lottery.parse_params(testCaseOne)
paramsTwo = lottery.parse_params(testCaseTwo)
paramsThree = lottery.parse_params(testCaseThree)

lotteriesAndProbabiliesOne = map(lambda x: (x[0], lottery.route_and_solve(x[1])), paramsOne)
lotteriesAndProbabiliesTwo = map(lambda x: (x[0], lottery.route_and_solve(x[1])), paramsTwo)
lotteriesAndProbabiliesThree = map(lambda x: (x[0], lottery.route_and_solve(x[1])), paramsThree)

print lottery.order(lotteriesAndProbabiliesOne)
print lottery.order(lotteriesAndProbabiliesTwo)
print lottery.order(lotteriesAndProbabiliesThree)


