from collections import Counter
def isAnagram(s, t):
    if len(s) != len(t):
        return False

    counerS= Counter(s)
    counterT = Counter(t)

    match = lambda counterS, counerT: all(key in counterT and counterS.get(key) == counterT.get(key) for key in counterT)

    return match(counerS,counterT)




s = "anagram"
t = "nagaram"

print(isAnagram(s,t))
