# SRM 157
# DIV 1
# 300
# 119.45 awarded
# p7
# wasted time fixing an off by one error

import math

class Salary():
    def howMuch(self, arrival, departure, wage):
        regRate = (float(wage) / 3600)
        plusRate = regRate * 1.5
        arrivalAndDeparture = zip(arrival, departure)
        payPeriods = map(lambda x: self.computePeriods(x[0], x[1]), arrivalAndDeparture)
        payments = map(lambda x: x[0]*plusRate + x[1]*regRate + x[2]*plusRate, payPeriods)
        
        return math.floor(reduce(lambda x,y: x+ y, payments))
        
        
    # tested
    def computePeriods(self, arrival, depart):
        pay = 0
        mornMin = 0
        arrival = self.toSeconds(arrival)
        depart = self.toSeconds(depart)
        mornMax = self.toSeconds('06:00:00')
        regMin = self.toSeconds('06:00:00')
        regMax = self.toSeconds('18:00:00')
        nightMin = self.toSeconds('18:00:00')
        nightMax = self.toSeconds('24:00:00')
        
        inMorn = 0
        inReg = 0
        inNight = 0
        if arrival < mornMax:
            inMorn = min(mornMax, depart)  - max(mornMin, arrival) 
        if arrival < regMax and depart >= regMin:
            inReg = min(regMax, depart) - max(regMin, arrival)
        if arrival < nightMax and depart >= nightMin:
            inNight = min(nightMax, depart) - max(nightMin, arrival)
            
        return (inMorn, inReg, inNight)
        
    # tested
    def toSeconds(self, time):
        seconds = 0
        time = time.split(':')
        seconds += int(time[0])*3600
        seconds += int(time[1])*60
        seconds += int(time[2])
        return seconds