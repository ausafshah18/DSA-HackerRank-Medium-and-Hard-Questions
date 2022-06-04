# Highest Value Palindrome -- HackerRank solution

def highestValuePalindrome(s, n, k):
    s = list(s)
    mark = [0]*n
    l = 0 # left index
    r = n-1 # right index
    while(l <= r):
        if(s[l] != s[r]):
            
            if(s[l] > s[r]):
                s[r] = s[l]
                mark[r] = 1
            else:
                s[l] = s[r]
                mark[l] = 1
            k -= 1
        l +=1
        r -=1
        
    if(k < 0):
        return "-1"
    
    # Maximize the digits
    l = 0
    r = n-1
    while(l <= r):
        if(l == r and k >= 1):
            s[l] = '9'
            break
        
        if(s[l] < '9'):
            # No changes before
            if(mark[l] == 0 and mark[r] == 0 and k >= 2): # changing both l and r for the first time
                s[l] = s[r] = '9'
                k-=2
            # Changed before
            if((mark[l] == 1 or mark[r] == 1) and k >= 1): # changing one of (l or r) for the first time or both of them for second time
                s[l] = s[r] = '9'
                k -= 1
        l += 1
        r -= 1
    return "".join(s)