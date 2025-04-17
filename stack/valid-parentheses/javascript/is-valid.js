const isValid = (s) => {
    // init stack
    const stack = [];

    // init default values with close
    const close_to_open = {')': '(', ']': '[', '}': '{'};

    // iterat over string
    for (let i = 0; i < s.length; i++) {
        const current_char = s[i];
        // check if current char is close
        if (close_to_open[current_char]) {
            if (stack.length > 0) {

                // get last element correspondent
                const last = stack[stack.length - 1];
                const correspondent = close_to_open[current_char];
    
                // compare with current char
                if (correspondent === last)
                    // remove from the stack
                    stack.pop();
                // return false
                else return false;
            } else return false;

        }
            // else add it to the stack
        else stack.push(current_char);
    }
    // check if stack is empty
    return stack.length === 0;
}