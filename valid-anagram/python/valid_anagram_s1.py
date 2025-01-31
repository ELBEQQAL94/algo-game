def isAnagram(s, t):
    newStringS = ''.join(sorted(s))
    print(newStringS)
    newStringT =  ''.join(sorted(t))
    print(newStringT)
    return newStringS == newStringT

s = "anagram"
t = "nagaram"
print(isAnagram(s,t))
