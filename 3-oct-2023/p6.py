from collections import Counter

def is_balanced_with_counter(expression):
    counter = Counter(expression)

    return counter['('] == counter[')']

expression = "((()))"
print(f"Is '{expression}' balanced? {is_balanced_with_counter(expression)}")
