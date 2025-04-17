function generateParenthesis(n) {
    const stack = [];
    const result = [];

    function backtrack(open, close) {

        if (open === close === n) {
            result.push(...stack);
            return;
        }
        
        // We can add an open parenthesis if we have not used all n open parentheses
        if (open < n) {
            stack.push('(');
            backtrack(open + 1, close);
        }
        
        if (close < open) {
            backtrack(current + ')', open, close + 1);
        }
    }
    
    backtrack('', 0, 0);
    
    return result;
}