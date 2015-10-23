# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # GREEDY
    # base case: list of length 1 is trivialy alternating
    # n = 2: alternating if a_2 has opposite polarity of a_1
    
    # valid init
    MAX = 0
    seq = []
    for i in xrange(0, len(A)):
        if A[i] != 0:
            # True -> +
            seq.append((A[i], A[i] > 0))
            MAX += 1
            break
        else:
            seq.append((A[i], A[i] > 0))
            MAX += 1
    
    for i in xrange(len(seq), len(A)):
        if A[i] == 0:
            seq.append((A[i], not seq[-1][1]))
        elif A[i] > 0 and seq[-1][1] == False:
            seq.append((A[i], A[i] > 0))
        elif A[i] < 0 and seq[-1][1] == True:
            seq.append((A[i], A[i] > 0))
        else:
            seq = [(A[i], A[i] > 0)]
        # print seq
        if len(seq) > MAX:
            MAX += 1
            
    return MAX