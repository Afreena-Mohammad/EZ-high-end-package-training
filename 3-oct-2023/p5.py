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

def is_balanced_with_stack(expression):
    stack = Stack()

    for char in expression:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.is_empty():
                return False
            else:
                stack.pop()

    return stack.is_empty()

expression = "((()))"
print(f"Is '{expression}' balanced? {is_balanced_with_stack(expression)}")
