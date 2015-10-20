# SRM 161
# DIV 1
# 300
# 157.05 awarded
# wasted time using strings instead of ints in tuple indices. forgot sorting intricacies
# use lamdas in parens, instead of wasting time writing a sortbykey function

class IsHomomorphism():
    def numBad(self, source, target, mapping):
        sourceMap = {}
        targetMap = {}
        for i in xrange(0, len(source)):
            for j in xrange(0, len(source[0])):
                sourceMap[(i,j)] = int(source[i][j])
                targetMap[(i,j)] = int(target[i][j])
                
        badPairs = []
        # test for homomorphism
        for i in xrange(0, len(source)):
            for j in xrange(0, len(source[0])):
                inDomain = mapping[sourceMap[(i,j)]]
                inRange = targetMap[(mapping[i], mapping[j])]
                if inDomain != inRange:
                    badPairs.append('(' + str(i) + ',' + str(j) + ')')
                    
        sortedByB = sorted(badPairs, reverse=False, key=self.sortByB)
        andSortedByA = sorted(sortedByB, reverse=False, key = self.sortByA)
        return tuple(andSortedByA)
        
    def sortByA(self, aTuple):
        return aTuple[0]
        
    def sortByB(self, aTuple):
        return aTuple[1]