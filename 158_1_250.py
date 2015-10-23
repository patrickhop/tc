# SRM 158
# DIV 1
# 250
# 91.71 awarded
# p7
# way too much trial and error coding...

class BaseMystery():
    def getBase(self, equation):
        # make alphabet table, and inverse table
        numToAlpha = {'0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', 
        '9':'9', '10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F', '16':'G',
        '17':'H', '18':'I', '19':'J'}
        alphaToNum = {}         
        for key in numToAlpha.keys():
            alphaToNum[numToAlpha[key]] = key
            
        # print alphaToNum
            
        # parse equation
        parsed = equation.split('+')
        a = parsed[0]
        b = parsed[1].split('=')[0]
        c = parsed[1].split('=')[1]
        
        # pad the shorter one
        if len(a) - len(b) > 0:
            for i in xrange(0, len(a) - len(b)):
                b = '0' + b
        elif len(b) - len(a) > 0:
            for i in xrange(0, len(b) - len(a)):
                a = '0' + a
                
        # make room for overflow
        a = '0' + a
        b = '0' + b
                
        base = 2
        bases = []
        while (base <= 20):
            mult = 0
            sum = ''
            for i in xrange(len(a) - 1, -1, -1):
                ai = int(alphaToNum[a[i]])
                bi = int(alphaToNum[b[i]])
                remain = (ai + bi + mult) % base
                mult = (ai + bi + mult) / base
                sum = numToAlpha[str(remain)] + sum
            # print 'base: ' + str(base) + ' ' + sum
            if sum == c or sum[1:] == c:
                bases.append(base)
            base += 1
        
        return tuple(bases)