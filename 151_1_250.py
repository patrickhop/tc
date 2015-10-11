# SRM 151
# DIV 1
# 250
# 141.42 awarded
# p4
# took some time to find sol. inverted theta calculatin bug

import math

class Archimedes():
    def approximatePi(self, numSides):
        # we are using the unit circle
        theta = math.pi / float(numSides)
        x_hat = 2*1*math.sin(theta)
        
        approx_perim = x_hat*numSides
        
        return approx_perim / 2.0