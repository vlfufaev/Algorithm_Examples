#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
#determine if the input string is valid.
#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.

class Solution(object):
    def isValid(self, s):
        stack = []
        if len(s) == 0:
            return True
        if len(s) % 2 == 1:
            return False
        stack.append(s[0])
        for k in range(1, len(s)):      
            if s[k] in ["(", "{", "["]:
                stack.append(s[k])
            else:
                if len(stack) == 0:
                    return False
                elif (s[k] == ")" and stack[-1] == "(") or (s[k] == "}" and stack[-1] == "{") or (s[k] == "]" and stack[-1] == "["):
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        else:
            return True

Example = Solution
s = "((([[[}}}"
print("Input string", s)
print("isValid = ", Example.isValid(Example, s))
