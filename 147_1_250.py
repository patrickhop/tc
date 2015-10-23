# SRM 148
# DIV 1
# 250
# 79.43 awarded
# p1
# didn't arrive at a simple solution quickly

class CircleGame:
    def cardsLeft(self, deck):
        valmap = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13}
        deck = filter(lambda x: valmap[x] != 13, list(deck))
        
        oldDeckLength = len(deck)
        while(True):
            for i in xrange(0, len(deck)):
                start = i
                end = i + 1
                # loop around
                if end > len(deck) - 1:
                    end = 0
                
                if valmap[str(deck[start])] + valmap[str(deck[end])] == 13:
                    deck[start] = 'K'
                    deck[end] = 'K'
        
            deck = filter(lambda x: valmap[x] != 13, deck)
            
            # detected a clean pass
            if oldDeckLength == len(deck):
                return len(deck)
        
            # update deck length
            oldDeckLength = len(deck)
        
            print deck
        
        return len(deck)
        
    def loop_around(self, start, end, max):
        if start == max + 1:
            start = 0
        
        if end == max + 1:
            end = 0
        elif end == max + 2:
            end = 1
        return start, end