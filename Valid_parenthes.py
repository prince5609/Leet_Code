def isValid(s):
    stack = []
    my_parentheses_dict = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in my_parentheses_dict:
            top_element = stack.pop() if stack else '#'
            if my_parentheses_dict[char] == top_element:
                return True
        else:
            stack.append(char)
    return not stack


print(isValid("([{}])"))
print(isValid("([{{])"))
