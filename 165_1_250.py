'''
SRM 165
DIV 1
250
177.67 awarded
was pretty smart about figuring out max-num proc to test
was understood two passes with the sort. pythons default sort is stable!
was good about recognizing the combination of the communication cost between processors
'''

import math

class ParallelSpeedup():
    def numProcessors(self, k, overhead):
        num_proc = 65
    
        comm = [] # (num_proc, comm)
        for i in xrange(1, num_proc + 1):
            if i == 1:
                comm.append((1,0))
            else:
                num_pairs = math.factorial(i) / float(2*math.factorial(i - 2))
                comm.append((i,num_pairs*overhead))
        
        times = map(lambda x: (x[0], x[1] + (k / x[0])), comm)
        sortedByNumProc = sorted(times, key=(lambda x: x[0]))
        return sorted(sortedByNumProc, key=(lambda x: x[1]))[0][0]