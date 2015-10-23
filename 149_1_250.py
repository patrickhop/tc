# SRM 149
# DIV 1
# 250
# 143.92 awarded
# p2
# spent too much time on one example case. focus more. no trial and error coding!

class BigBurger():
    def maxWait(self, arrival, service):
        pairs = zip(arrival, service)
        
        busyUntil = 0
        waits = []
        for i in xrange(0, len(pairs)):
            arrival = pairs[i][0]
            wait = -1
            if busyUntil == 0:
                wait = 0
            else:
                wait = max(busyUntil - arrival, 0)
                
            waits.append(wait)
            busyUntil = max(busyUntil, arrival) + pairs[i][1]
            
        return max(waits)