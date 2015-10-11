# SRM 152
# DIV 1
# 250
# 117.84 awarded
# p4
# this just took awhile to get right...

class LeaguePicks():
    def returnPicks(self, position, friends, picks):
        myPicks = []
        numPicked = 1
        hasReversed = False
        while numPicked < picks:
            if hasReversed == False:
                for i in xrange(1, friends + 1):
                    #print i
                    if i == position:
                        myPicks.append(numPicked)
                    numPicked += 1
                hasReversed = True
            elif hasReversed == True:
                for i in xrange(friends, 0, -1):
                    #print i
                    if i == position:
                        myPicks.append(numPicked)
                    numPicked += 1
                hasReversed = False
        
        return tuple(myPicks)