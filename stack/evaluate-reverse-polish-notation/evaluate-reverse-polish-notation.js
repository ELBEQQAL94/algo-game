const plus = (a, b) => parseInt(a + b);
const sub = (a, b) => parseInt(a - b);
const multi = (a, b) => parseInt(a * b);
const div = (a, b) => parseInt(a / b);

const PLUS = "+";
const SUB = "-";
const MULTI = "*";
const DIV = "/";

const evalRPN = (tokens) => {
    const stack = [];
    
    for (let i = 0; i < tokens.length; i++) {
        const current_element = tokens[i];
        if (isNaN(+current_element)) {
            if (stack.length > 0) {
                const b = stack.pop();
                const a = stack.pop();        

                if (current_element === PLUS) {
                    const result = plus(a, b);
                    stack.push(result);
                }

                if (current_element === SUB) {
                    const result = sub(a, b);
                    stack.push(result);
                }

                if (current_element === MULTI) {
                    const result = multi(a, b);
                    stack.push(result);
                }

                if (current_element === DIV) {
                    const result = div(a, b);
                    stack.push(result);
                }
            }
        } else {
            stack.push(+current_element);
        }
    }

    const result = stack.at();
    return result;
};

// const tokens = ["2","1","+","3","*"];
// const tokens = ["4","13","5","/","+"];
const tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
evalRPN(tokens);