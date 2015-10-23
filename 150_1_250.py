# SRM 149
# DIV 1
# 250
# 87.19 awarded
# p3
# this just took awhile to get right...

import math

class InterestingDigits():
    def digits(self, base):
    
        # setup. remove when disproven
        interestingNumbers = []
        for i in xrange(2, base):
            interestingNumbers.append(i)
        
        
        for i in xrange(0, 2):
            for j in xrange(0, base):
                for k in xrange(1, base):
                    for m in interestingNumbers:
                        # exlude [0,9]
                        if i == 0 and k == 0:
                            break
                            
                        maybeInteresting = m*math.pow(base, 0)
                        number = (i*math.pow(base, 2) + j*math.pow(base, 1) + k*math.pow(base, 0))
                        ii, jj, kk = self.multiply(base, i, j, k, m)
                        if ((ii + jj + kk) % m) != 0:
                            interestingNumbers.remove(m)
                            # print ''
                            # print str(i) + str(j) + str(k)
                            # print 'removing: ' + str(m) + ' because of number: ' + str(ii) + str(jj) + str(kk)
                            break
                            
        # print 'dumping interesting numbers'
        # print interestingNumbers
        return tuple(interestingNumbers)
    
        
        
    def multiply(self, base, i, j, k, m):
        kOverflow = m*k / base
        jOverflow = m*j / base
        
        k = m*k % base
        j = (m*j % base) + kOverflow
        i = (m*i % base) + jOverflow
        
        return i, j, k