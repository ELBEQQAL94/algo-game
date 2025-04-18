def isValid(s):
    hasmap = {'(':')', '{':'}', '[':']' }
    stack = []
    
    # check if stack is not empty
    if len(s) == 1: return False

    # iterate over string and chec if open
    for char in s:
        # check if char is open
        if char in hasmap: # [
            # add it to the stack
            stack.append(char)
        else:
            if len(stack) == 0: return False
            # if close return  lastitem value from hashmap 
            lastItem = stack[-1] # (
            value = hasmap[lastItem] # )
            # check if equal remove from the stack
            if value != char: # value = ), char = )
                stack.append(char) 
            else: stack.pop() 
    return len(stack) == 0

# s1 = "()" # True
# print(isValid(s1))

# s2 = "()[]{}" # true
# print(isValid(s2))

# s3 = "(]" # false
# print(isValid(s3))

# s4 = "([])" # true
# print(isValid(s4))

# s5 = "["
# print(isValid(s5)) # False

# s6 = "]"

# print(isValid(s6)) # False

# s7 = "){"

# print(isValid(s7)) # False

s8 = ")(){}"

print(isValid(s8)) # False
