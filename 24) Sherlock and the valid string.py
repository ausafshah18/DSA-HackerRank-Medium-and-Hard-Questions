# Sherlock and the valid string -- HackerRank Solution

from collections import Counter

def isValid(s):
    c = Counter(s)
    if len(set(c.values())) == 1:
        return "YES"
    elif len(set(c.values())) > 2: # We can't reduce character in more than one type
        return "NO"
    else:     # If only 2 different counts present. Means we can reduce higher one to make them equal
        for i in c:
            c[i] -= 1 # first we reduce and check if now the length of chars will be equal
            temp = list(c.values())
            
            try:
                temp.remove(0) # it tries this
            except:
                pass # if above condition fails in removing zeroes then we goto next iteration
            if len((set(temp))) == 1:
                return "YES"
            else:
                c[i] += 1 # if we fail we again make it original
        return "NO"