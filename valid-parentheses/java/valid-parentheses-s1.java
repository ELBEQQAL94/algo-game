package org.main.algo.stack;

import java.util.ArrayList;
import java.util.HashMap;

public class ValidParentheses {
    public boolean isValid(String s) {
        // Create a stack to store opening brackets
        ArrayList<Character> stack = new ArrayList<>();

        // Map to store closing brackets with their corresponding opening brackets
        HashMap<Character, Character> close_to_open = new HashMap<>();
        close_to_open.put(')', '(');
        close_to_open.put('}', '{');
        close_to_open.put(']', '[');

        // Loop through each character in the string
        for (int i = 0; i < s.length(); i++) {
            char current_value = s.charAt(i);

            // Check if the character is a closing bracket
            if (close_to_open.containsKey(current_value)) {
                // Get the corresponding opening bracket
                char value_of_last_element = close_to_open.get(current_value);

                // Check if the stack is not empty and the last element matches the opening bracket
                if (!stack.isEmpty()) {
                    char last_element = stack.get(stack.size() - 1);
                    if (value_of_last_element == last_element) {
                        // Remove the last element from the stack
                        stack.remove(stack.size() - 1);
                    } else {
                        // Mismatch found, return false
                        return false;
                    }
                } else {
                    // Stack is empty when closing bracket is found, return false
                    return false;
                }
            } else {
                // If it's an opening bracket, add it to the stack
                stack.add(current_value);
            }
        }

        // If the stack is empty, return true (valid parentheses); otherwise, return false
        return stack.isEmpty();
    }
}
