# Two Characters -- HackerRank Solution
def alternate(s):
    maxcount = count = 0
    myset = list(set(s))
    
    for i in range(len(myset)):
        for j in range(i+1,len(myset)): # through these nested loops we are generating pairs
            mylist = [myset[i],myset[j]]
            
            if s.index(myset[i]) < s.index(myset[j]):
                ind = 0
            else:
                ind = 1
                
            for char in s:
                if char in mylist: # checking if this particular char is present in mylist
                    if char == mylist[ind]:
                        count += 1
                        ind = ind^1 # this is xor operation. if ind is 0 the, o^1=1. And if ind is 1 then, 1^0=0. This way we keep checking if the two characters are appearing alternatively
                    else:
                        count = 0
                        break
            
            maxcount = max(maxcount,count)
            count = 0
    return maxcount