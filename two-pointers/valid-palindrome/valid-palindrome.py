def isPalindrome(s):
    clean_string = ''.join([char for char in s if char.isalnum()]).lower()
    left = 0
    right = len(clean_string) - 1
 
    while left < right:
       if clean_string[left] != clean_string[right]:
           return False
       
       left += 1
       right -=1
    return True