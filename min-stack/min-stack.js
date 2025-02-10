class MinStack {
    
    stack = [];

    // push
    push(val) {
        this.stack.push(val);
    }

    // top
    top() {
        return this.stack[this.stack.length - 1];
    }

    // pop
    pop() {
        this.stack.pop();
    }

    // getMin
    getMin() {
        return Math.min(...this.stack);
    }
}
