package org.main;

import org.main.algo.stack.ValidParentheses;

import java.util.Stack;

public class Main {


    public static boolean isNumeric(String str) {
        return str != null && str.matches("-?\\d+(\\.\\d+)?");
    }

    public static int plus(int a, int b){
        return a+b;
    }
    public static int multi(int a, int b){
        return a*b;
    }
    public static int div(int a, int b){
        return a/b;
    }
    public static int minus(int a, int b){
        return a-b;
    }

    final static String PLUS = "+";
    final static String MULTI = "*";
    final static String DIV = "/";
    final static String MINUS = "-";
    public static int evalRPN(String[] tokens){
        Stack stack = new Stack<Integer>();

        for(int i=0 ; i< tokens.length ; i++){
            String current_string = tokens[i];
            if(!isNumeric(current_string)){
                int b = (int) stack.pop();
                int a = (int) stack.pop();

                if(current_string.equals(MINUS)){
                    int result = minus(a,b);
                    stack.push(result);
                }
                if(current_string.equals(PLUS)){
                    int result = plus(a,b);
                    stack.push(result);
                }
                if(current_string.equals(DIV)){
                    int result = div(a,b);
                    stack.push(result);

                }
                if(current_string.equals(MULTI)){
                    int result = multi(a,b);
                    stack.push(result);
                }

            }
            else{
                stack.push(Integer.parseInt(current_string));
            }
        }
     return (int)stack.pop();
    }
    public static void main(String[] args) {
        System.out.println("Hello world!");
        ValidParentheses validator = new ValidParentheses();
        String str = ")(){}";
        boolean isValid = validator.isValid(str);
        System.out.println(isValid);

    }
}