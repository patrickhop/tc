# SRM 153
# DIV 1
# 250
# 190.18 awarded
# p5
# did well understanding and decomposing problem. functional approach was great

import math

class Inventory():
    def monthlyOrder(self, sales, daysAvailable):
        salesAndAvails = zip(sales, daysAvailable)
        salesAndAvails = filter(lambda x: x[0] != 0, salesAndAvails)
        scaled = map(lambda x: (30.0*float(x[0]) / float(x[1])), salesAndAvails)
        average = reduce(lambda x,y: x + y, scaled) / len(scaled)
        
        return math.ceil(average - 0.000000001)