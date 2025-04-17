// Valid Parentheses using built in Stack instead of ArrayList
    public boolean isValid(String s) {
        // init stack
        Stack<Character> stack = new Stack<>();
        // init default values with close
        HashMap<Character, Character> open_to_close = new HashMap<>();

        open_to_close.put(')', '(');
        open_to_close.put('}', '{');
        open_to_close.put(']', '[');

        // iterate over string
        for (int i = 0; i < s.length(); i++) {
            // get current char
            char current_char = s.charAt(i);
            // check if close
            if (open_to_close.containsKey(current_char)) {
                // check if stack is not empty
                if (!stack.empty()) {
                    // get last element correspondent
                    char last_element = stack.lastElement();
                    // compare last element correspondent with current value
                    char correspondent_value = open_to_close.get(current_char);
                    if (correspondent_value == last_element) {
                        // if it matched remove from stack
                        stack.pop();
                        // else return false
                    } else return false;

                    // else return false
                } else return  false;
            }
            // else add to the stack
            else  stack.add(current_char);
        }
        // check if stack empty
        return stack.empty();
    }