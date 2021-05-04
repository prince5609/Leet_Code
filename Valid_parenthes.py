class Solution:
    def isValid(self, s):
        stack = []
        my_parenthes_dict = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in my_parenthes_dict:
                top_element = stack.pop() if stack else '#'
                if my_parenthes_dict[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

obj = Solution()
print(obj.isValid("([{}])"))




























