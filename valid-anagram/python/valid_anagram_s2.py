def isAnagram(s, t):
    counter = 0
    for char in range(len(s)):
        print(s[char])
        if s[char] in t:
            counter += 1
    
    if counter == len(t):
        return True
    return False

s = "anagram"
t = "nagaram"
print(len(t))
print(isAnagram(s, t))



