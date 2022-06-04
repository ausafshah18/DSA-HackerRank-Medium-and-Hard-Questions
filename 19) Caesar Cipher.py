# Caesar Cipher  -- HackerRank Solution
def caesarCipher(s, k):
    result = []
    for i in range(len(s)):
        result.append(ord(s[i]))
        
    for i in range(len(s)):
        if(result[i] >= 65 and result[i] <= 90): # lower case letters range from ascii values 65-90
            result[i] = (65 + (result[i] - 65 + k) % 26)  # if after adding k value goes above 90 then it goes adding from 65 as aksed in the question
        elif(result[i] >= 97 and result[i] <= 122): # upper case letters range from ascii values 97-122
            result[i] = (97 + (result[i] - 97 + k) % 26)
    return "".join(map(chr,result)) # map is a function using it we put each element of result[] in chr() and convert it into character
