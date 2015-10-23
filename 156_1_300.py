# SRM 156
# DIV 1
# 300
# 118.20 awarded
# p6
# mixed up rows and columns. wasted lots of time on a bug-hunt

class BombSweeper():
    def winPercentage(self, board):
        mat = map(lambda x: list(x), board)
        wins = 0
        losses = 0
        
        
        # iterate over columns
        for i in xrange(0, len(mat[0])):
            # iterate over rows
            for j in xrange(0, len(mat)):
                if mat[j][i] == 'B':
                    losses += 1
                else:
                    validNeighbors = self.getValidNeighbors(mat, i, j)
                    didLose = False
                    for neighbor in validNeighbors:
                        if mat[neighbor[0]][neighbor[1]] == 'B':
                            didLose = True
                            break
                    # no bad neighbors found => win
                    if didLose == False:
                        wins += 1
                    
        print wins
        print losses
        
        return (float(wins) / (float(wins) + float(losses))) * 100
        
    def getValidNeighbors(self, mat, colIndex, rowIndex):
        maxRowIndex = len(mat) - 1
        maxColumnIndex = len(mat[0]) - 1
        
        # enumerate to save time.
        neighborIndices = []
        neighborIndices.append((rowIndex + 1, colIndex + 1))
        neighborIndices.append((rowIndex + 1, colIndex))
        neighborIndices.append((rowIndex + 1, colIndex - 1))
        neighborIndices.append((rowIndex, colIndex + 1))
        neighborIndices.append((rowIndex, colIndex - 1))
        neighborIndices.append((rowIndex - 1, colIndex + 1))
        neighborIndices.append((rowIndex - 1, colIndex))
        neighborIndices.append((rowIndex - 1, colIndex - 1))
        
        # filter bad tuples
        neighborIndices = filter(lambda x: x[0] <= maxRowIndex and x[0] >= 0, neighborIndices)
        return filter(lambda x: x[1] <= maxColumnIndex and x[1] >= 0, neighborIndices)