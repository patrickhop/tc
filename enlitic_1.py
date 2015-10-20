# find min-subsequence of length two s.t elements of subsequence are non-adjacent
# endpoints aren't of interest. we can safely exclude them from sequence, and base-case computation
# n = 1 (no sol: no subsequence of length two)
# n = 2 (no sol: elements of subsequence must be adjacent)
# n = 3 (sol : opt = [(A_0, 0), (A_2, 2)]) => Base Case... sol contains all data need to compute optimality
# n = n + 1 (sol: produce new-subsequence that is optimal for n + 1
def solution(A):
    A = A[1:-1] # endpoints are not of interest to us
    opt = [(A[0], 0), (A[2], 2)] # Base case
    for i in xrange(3, len(A)):
        if A[i] < opt[0][0] and A[i] < opt[1][0]:
            if i + 1 != opt[1][1]:
                # not adj
                if opt[0][0] >= opt[1][0]:
                    opt[0] = opt[1]
                    opt[1] = (A[i], i)
                else:
                    opt[1] = (A[i], i)
            else:
                # is adj
                opt[1] = (A[i], i)
        elif A[i] < opt[1][0]:
            # adjacency doesn't matter
            opt[1] = (A[i], i)
        elif A[i] < opt[0][0] and (i + 1 != opt[1][1]):
            # if it's adjacent, we can't replace first element
            opt[0] = opt[1]
            opt[1] = (A[i], i)
            
    return opt[0][0] + opt[1][0]