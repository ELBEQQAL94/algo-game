/**
 * Generate all combinations of well-formed parentheses for a given number of pairs
 * @param {number} n - Number of pairs of parentheses
 * @return {string[]} - Array of all valid parentheses combinations
 */
function generateParenthesis(n) {
    const result = [];
    
    // Helper function to perform backtracking
    function backtrack(currentString, openCount, closeCount) {
        // Base case: we've used all parentheses
        if (openCount === n && closeCount === n) {
            result.push(currentString);
            return;
        }
        
        // Option 1: Add an opening parenthesis if we haven't used all n
        if (openCount < n) {
            backtrack(currentString + '(', openCount + 1, closeCount);
        }
        
        // Option 2: Add a closing parenthesis if valid
        // We can only add a closing parenthesis if there are unclosed opening parentheses
        if (closeCount < openCount) {
            backtrack(currentString + ')', openCount, closeCount + 1);
        }
    }
    
    // Start the backtracking with an empty string and 0 counts
    backtrack('', 0, 0);
    
    return result;
}

// Example usage:
// console.log(generateParenthesis(3));
// Output: ["((()))","(()())","(())()","()(())","()()()"]

console.log(generateParenthesis(1));
// Output: ["()"]

// Additional test case
// console.log(generateParenthesis(2));
// Output: ["(())","()()"]