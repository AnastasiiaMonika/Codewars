"""
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""

def find_short(s):
    minlen = 100000
    leng = 0
    for i in s:
        if i == ' ':
            minlen = leng if (leng < minlen) | (minlen == 0) else minlen
            leng = 0
        else:
            leng +=1
    return leng if (leng < minlen) | (minlen == 0) else minlen # l: shortest word length


#def find_short(s):
#    return min(len(x) for x in s.split())

s = "Hello"
print(find_short(s))