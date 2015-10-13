# SRM 160
# DIV 1
# 250
# 155.04 awarded
# was thoughtful in solution. lost some time dealing with rounding.

import math

class Iditarod():
    def avgMinutes(self, times):
        times = map(lambda x: self.parseTime(x), times)
        timesInMin = map(lambda x: self.toMinutes(x), times)
        return round((float(reduce(lambda x,y: x + y, timesInMin)) / float(len(times))))
    
    def toMinutes(self, time):
        minutes = 0
        minutes += time[0]*1440
        minutes += (time[1] % 12)*60 - 8*60
        if time[3] == 'PM':
            minutes += 12*60
        minutes += time[2]
        return minutes
    
    # seems to work (tested)
    def parseTime(self, time):
        splitOnColon = time.split(':')
        splitOnSpace = splitOnColon[1].split(' ')
        
        hours = int(splitOnColon[0])
        mins = int(splitOnSpace[0])
        state = splitOnSpace[1][0:2]
        days = int(splitOnSpace[3]) - 1
        return (days, hours, mins, state)