# SRM 145
# DIV 1
# 250
# 110 awarded

import math

class Bonuses():
    def getDivision(self, points):
        totalPoints = reduce(lambda x,y: x+y, points)
        percentages = map(lambda x: self.truncated_percentage(x, totalPoints), points)
        leftover = 100 - reduce(lambda x,y: x+y, percentages)
                
        # save the indices of the max indices
        nMaxPoints = [0 for x in range(leftover)]
        nMaxIndices = [0 for x in range(leftover)]
        for i in xrange(0, len(points)):
            for j in xrange(0, leftover):
                if points[i] > nMaxPoints[j]:
                    nMaxPoints.insert(j, points[i])
                    nMaxIndices.insert(j, i)
                    if len(nMaxPoints) > leftover:
                        nMaxPoints.pop()
                        nMaxIndices.pop()
                    break
        
        # increment payouts
        for index in nMaxIndices:
            percentages[index] += 1
            
        # print percentages
            
        return percentages
        
    def truncated_percentage(self, points, totalPoints):
        percentage = float(points) / float(totalPoints)
        return int(math.floor(100*percentage))