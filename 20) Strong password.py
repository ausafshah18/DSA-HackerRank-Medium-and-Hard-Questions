# Strong Password -- HackerRank Solution
def minimumNumber(n, password):
    spl = '!@#$%^&*()-+' # special characters
    l = [0,0,0,0]
    
    for char in password:
        if char.isdigit():
            l[0] = 1
        elif char.islower():
            l[1] = 1
        elif char.isupper():
            l[2] = 1
        elif char in spl: # checks in spl
            l[3] = 1
            
    res = max(6-n,4-sum(l)) # we have to return max of these two. Check out sample cases
    if res < 0:
        return 0
    else:
        return res