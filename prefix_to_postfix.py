class Solution:
    def postToInfix(self , s):
        stack = []

        for char in range(len(s) -1 , -1 , -1):
            char = s[char]
            if char.isalnum():
                stack.append(char)
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()
                new_expr = "".join(f"{operand1}{operand2}{char}")
                stack.append(new_expr)

        return stack[-1]

sol = Solution()
expr = "/-AB*+DEF"
print(sol.postToInfix(expr))