'''
SRM 164
DIV 1
300
118.34 awarded
had to write lots and lots of code to handle all of the test cases. perhaps there is a simpler solution?
'''

class UserId():
    def id(self, inUse, first, middle, last):
        # check isValid func
        # print self.isValid('hello', 'world', 'yo')
        # print self.isValid('a', 'bb', 'cc')
        # print self.isValid('hello', '', 'world')
        # print self.isValid(' hello', '', '\'world')
        # print self.isValid('hello9', 'something', 'world')
        
        # figure out a smarter way to do this...
        first = first.replace('\'', '').replace(' ', '').lower()
        middle = middle.replace('\'', '').replace(' ', '').lower()
        last = last.replace('\'', ' ').replace(' ', '').lower()
        
        if self.isValid(first, middle, last) == True:
            if (first[0] + last)[:8] not in inUse:
                if len(first[0] + last) > 8:
                    return (first[0] + last)[:8]
                else:
                    return first[0] + last
            elif len(middle) != 0:
                if (first[0] + middle[0] + last)[:8] not in inUse:
                    if len(first[0] + middle[0] + last) > 8:
                        return (first[0] + middle[0] + last)[:8]
                    else:
                        return (first[0] + middle[0] + last)
            
            # find availible digit
            digits = 1
            while (True):
                if len(str(digits)) == 1 and ((first[0] + last)[:6] + '0' + str(digits)) not in inUse:
                    if (first[0] + last) > 6:
                        return (first[0] + last)[:6] + '0' + str(digits)
                    else:
                        return (first[0] + last + '0' + str(digits))
                elif len(str(digits)) == 2 and ((first[0] + last)[:6] + str(digits)) not in inUse:
                    if (first[0] + last) > 6:
                        return (first[0] + last)[:6] + str(digits)
                    else:
                        return first[0] + last + str(digits)
                digits += 1
        
        return 'BAD DATA'
        
    def isValid(self, first, middle, last):
        valid = False
        # check length
        if len(first) >= 2 and len(last) >= 2:
            id = list(first.upper() + middle.upper() + last.upper())
            id = map(lambda x: ord(x), id)
            # print id
            valid = True
            for i in xrange(0, len(id)):
                # check for valid chars
                if id[i] not in range(65,92) and id[i] != ord('\'') and id[i] != ord(' '):
                    valid = False
        return valid