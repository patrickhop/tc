# SRM 155
# DIV 1
# 300
# 126.35 awarded
# p5
# messed up original design. stupid mistakes

class PaternityTest():
    def possibleFathers(self, child, mother, men):
        indices = []
        
        for i in xrange(0, len(men)):
            childMother = zip(child, mother)
            temp = zip(childMother, men[i])
            childMotherFather = map(lambda x: (x[0][0], x[0][1], x[1]), temp)
            notInFather = filter(lambda x: x[0] != x[1] and x[0] != x[2], childMotherFather)
            inFather = filter(lambda x: x[0] == x[2], childMotherFather) 
        
            # print len(inFather)
            if len(notInFather) == 0 and float(len(inFather)) / len(child) >= .5:
                indices.append(i)
        
        return tuple(indices)