# Super Reduced String -- HackerRank Solution
def superReducedString(s):
    result = []
    for i in range(len(s)):
        if len(result) == 0 or result[-1] != s[i]:
            result.append(s[i])
        else:
            result.pop()
    if(len(result) == 0):
        return "Empty String"
    else:
        return "".join(result) # it will concatenate the characters and return us a string