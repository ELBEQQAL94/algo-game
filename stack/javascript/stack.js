// Implenet Stack Datastructure
// Stack from scratch
class Stack {
    stack = [];
    limit = 5;
    
    // Push
    push(element) {
        !this.isFull() && this.stack.push(element); // condition and expression
    }
    
    // Pop
    pop() {
        !this.isEmpty() && this.stack.pop();
    }
    
    // IsEmpty
    isEmpty() {
        return this.stack.length === 0;
    }
    
    // IsFull
    isFull() {
        return this.stack.length === this.limit;
    }
    
    // Peek or Top
    peek() {
        return !this.isEmpty() && this.stack[this.stack.length - 1];
    }

    // display current stack data
    logStack() {
        return this.stack;
    }
}

// Usage
const s = new Stack();

const old_stack = s.logStack();

console.log('old_stack', old_stack);

s.push(1);
s.push(2);
s.push(3);
s.push(4);
s.push(5);

console.log("peek: ", s.peek());

const current_stack = s.logStack();

console.log('current_stack', current_stack);
