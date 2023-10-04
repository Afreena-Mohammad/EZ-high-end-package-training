def is_balanced_with_count(expression):
    count = 0

    for char in expression:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1

        if count < 0:
            return False

    return count == 0

expression = "{[()]}"
print(f"Is '{expression}' balanced? {is_balanced_with_count(expression)}")
