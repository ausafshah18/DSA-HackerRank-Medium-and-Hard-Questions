# The Love-Letter Mystery HackerRank solution

def theLoveLetterMystery(s):
    i = 0
    count = 0
    j = len(s)-1
    while(i < j): 
        if s[i] != s[j]:
            count += abs( ord(s[i]) - ord(s[j]) ) # we don't decrease each character but we increase count by the difference in ASCII values. ord() gives ascii values
        i+= 1
        j-=1
    return count