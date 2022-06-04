# Palindrome Index -- HackerRank Solution
def palindromeIndex(s):
    if s == s[::-1]:
        return -1
    n = len(s)

    # We will compare first and last elements and when elements are not same we pick substrings and check which one is pailindrome. 
    for i in range(n):
        if (s[i] != s[n-1-i]):  
            if s[i:n-1-i] == s[i:n-1-i][::-1]: # s[i:n-1-i][::-1] means inverse of s[i:n-1-i]. example: aabcbdaa , here bcb == bcb
                return n-1-i
            elif s[i+1:n-i] == s[i+1:n-i][::-1]:  # example: aakcbcaa , here cbc == cbc.
                return i

# If You don't understand this code watch: https://www.youtube.com/watch?v=gd4hCrbYAMg 