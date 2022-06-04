# Anagram HackerRank Solution
from collections import Counter # Counter makes a dictionary to store values
def anagram(s):
    if len(s)%2 != 0:
        return -1
    n = len(s)//2
    s = Counter(s[ :n]) - Counter(s[n: ]) # We subtract the two dictionaries.The same chars will be subtracted and become zero. s will now store a dictionary
    return sum(s.values()) # values() conatains the number of elements in the dictionary. This way we get the non common elements in the two strings