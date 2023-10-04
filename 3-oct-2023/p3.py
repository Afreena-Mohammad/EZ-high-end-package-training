class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def size(self):
        return len(self.items)

# Example usage
stack = Stack()

# Pushing items onto the stack
stack.push(5)
stack.push(10)
stack.push(15)

# Peeking at the top item
print("Top item:", stack.peek())

# Popping items from the stack
print("Popped:", stack.pop())
print("Popped:", stack.pop())

# Checking if the stack is empty
print("Is stack empty?", stack.is_empty())
