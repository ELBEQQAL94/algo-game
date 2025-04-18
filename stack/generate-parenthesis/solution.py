def generateParenthesis(n):
    result = []
    
    def backtrack(current_string, open, close):
        if len(current_string) == 2*n:
            result.append(current_string)
            return
        
        if open < n:
            backtrack(current_string + '(', open + 1, close)

        if close < open:
            backtrack(current_string + ')', open, close + 1)
        
        
    backtrack('', 0, 0)

    return result