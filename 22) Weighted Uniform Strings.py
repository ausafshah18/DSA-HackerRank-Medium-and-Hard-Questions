# Weighted Uniform Strings -- HackerRank Solution
def weightedUniformStrings(s, queries):
    weight = 0
    d = {}
    
    for i in range(len(s)):
        if i == 0 or s[i] != s[i-1]: # if no repetition occurs like 'ccc'
            weight = ord(s[i])-ord('a')+1
        else:  # if repetition occurs like 'ccc'
            weight = (weight + ord(s[i])-ord('a')+1)
        d[weight] = 1 # storing weight in dictionary
    
    result = []
    for q in queries:
        if q in d:
            result.append("Yes")
        else:
            result.append("No")
    return result