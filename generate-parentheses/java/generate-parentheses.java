package org.main.algo.stack;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class GenerateParentheses {

    List<String> result = new ArrayList<>();
    Stack<Character> stack = new Stack<>();
    public List<String> generateParenthesis(int n) {

        backtrack(0,0 , n);
        return result;

    }

        private void backtrack(int open , int close, int n){
            if(open == n && close == n){
                String str = convertStackToString(stack);
                result.add(str);
                return;
            }
            if(open < n){
                stack.push('(');
                backtrack(open + 1, close, n);
                stack.pop();
            }
            if(open < close) {
                stack.push(')');
                backtrack(open, close + 1 , n);
                stack.pop();
            }

        }

        private String convertStackToString(Stack<Character> stack){
           String result = "";
          for(int i = 0 ; i < stack.size() ; i++){
              result += stack.get(i);

          }
         return result;
        }

}

 