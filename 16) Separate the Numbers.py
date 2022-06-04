# Separate the Numbers HackerRank Probelm

def separateNumbers(s):
    if len(s) == 0:
        print("NO")
    else:
        for i in range(1,len(s)//2+1):
            mystr = s[:i]
            prev = int(mystr)
            while(len(mystr) < len(s)):
                prev = prev + 1
                next = str(prev)
                mystr = mystr + next 
            if mystr == s:
                first = s[:i]
                print("YES",first)
                return
        print("NO")
        return