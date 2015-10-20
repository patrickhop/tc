#Several years ago you took a trip that went through many cities, but you can't remember all the details.  You remember that you started and ended at different cities, and went through a number of cities in between, but never went to a city twice.  Luckily, you've found a jumbled bag of your own plane ticket stubs.  Unluckily, your dog found them -- not only are they in a random order, but all information except for the origin and destination cities have been gnawed off.  For example, perhaps you have plane stubs
#LHR -> CDG
#SFO -> JFK
#BOS -> LAX
#JFK -> MIA
#CDG -> BOS
#MIA -> LHR

#Task 1: In which city did the trip begin?

#Task 2: Reconstruct the entire itinerary

def make_itinerary(tickets):
    departureTable = {}
    for ticket in tickets:
        departureTable[ticket[0]] = ticket[1]

    arrivalTable = {}
    for ticket in tickets:
        arrivalTable[ticket[1]] = ticket[0]
        
    # walk forward
    sol = [ticket[0], ticket[1]]
    tickets = tickets[1:]
    
    
    for i in xrange(0, len(tickets)):
        head = sol[0]
        tail = sol[-1]
        
        # prepend
        if head in arrivalTable.keys():
            sol.insert(0, arrivalTable[head])
           
        
    for i xrange(0, len(tickets)):
        # append
        head = sol[0]
        tail = sol[-1]
        
        if tail in departureTable.keys():
            sol.append(depatureTable[tail])
             
# MIA -> LHR -> CDG -> BOS
        

'''
itinerary = list(tickets[0])
tickets = tickets[1:]
for ticket in tickets:
    head = itinerary[0][0]
    tail = itinerary[-1][1]
    
    if ticket[1] == head:
        # prepend
        itinerary.insert(0, ticket)
    elif ticket[1] == tail:
        # append
        itinerary.append(ticket)
        
'''



The sum below is expressed only in letters. A stands for one of the digits 1 through 9, B for another, and C for yet another. 
Given the sum, what must A, B and C be?
      A  A    
+     B  B
 ---------
=  C  B  C

AA = A*10^1 + A*10^0
BB = B*10^1 + B*10^0

CBC = C*10^2 + B*10^1 + C*10^0

A*10^1 + A*10^0 + B*10^0 = C*10^2 + C*10^0
11*A + B = 101*C

A = 9
B = 2
C = 1

99 + 2 = 101*1
