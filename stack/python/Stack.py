class Stack:
    def __init__(self, limit=3):  # Initialize stack with a size limit
        self.stack = []
        self.limit = limit
    
    def push(self, element):
        """Add an element to the stack if it's not full."""
        if not self.isFull():
            self.stack.append(element)
        else:
            print("Stack is full. Cannot push.")
    
    def pop(self):
        """Remove and return the top element if the stack is not empty."""
        if not self.isEmpty():
            return self.stack.pop()
        print("Stack is empty. Cannot pop.")
    
    def isEmpty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0
    
    def isFull(self):
        """Check if the stack is full."""
        return len(self.stack) == self.limit
    
    def top(self):
        """Show the top element without removing it."""
        if not self.isEmpty():
            print(self.stack[-1])
        else:
            print("Stack is empty.")
    
    def display(self):
        """Display all elements in the stack."""
        print(self.stack)

# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)  # This will show "Stack is full"
stack.display()
stack.pop()
stack.top()
stack.display()