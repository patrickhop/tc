'''
SRM 163
DIV 1
250
138.23 awarded
took some time to understand the problem. architecture was sound. lost some time with using stacks correctly
'''

class Rochambo():
    def wins(self, opponent):
        wins = 0
        stack = []
        didWin = {('P','P'):'TIE', ('P','R'):'WIN', ('P','S'):'LOSE', ('S','S'):'TIE',
        ('S','P'):'WIN', ('S','R'):'LOSE', ('R','R'):'TIE', ('R','S'):'WIN', ('R', 'P'):'TIE'}
        getWin = {'P':'S', 'S':'R', 'R':'P'}
        
        # compute base
        stack.append(opponent[0])
        stack.append(opponent[1])
        if didWin[('R', opponent[0])] == 'WIN':
            wins += 1
        if didWin[('R', opponent[1])] == 'WIN':
            wins += 1
            
        opponent = opponent[2:]
        for i in xrange(0, len(opponent)):
            move = 'na'
            # homogenous and hetereogenous cases
            if stack[0] == stack[1]:
                move = getWin[stack[1]]
            else:
                choices = ['P', 'S', 'R']
                choices.remove(stack[0])
                choices.remove(stack[1])
                move = getWin[choices[0]]
                
            if didWin[(move, opponent[i])] == 'WIN':
                wins += 1
            stack.pop(0)
            stack.append(opponent[i])
                
        return wins