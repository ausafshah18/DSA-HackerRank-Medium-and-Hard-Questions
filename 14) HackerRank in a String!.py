# HackerRank in a String!--- HackerRank solution
def hackerrankInString(s):
    s2 = "hackerrank"
    m = len(s2)
    i = 0
    for char in s: # traverses whole s 
        if char == s2[i]:
            i = i+1
        if i == m:
            return "YES"
        
    return "NO"