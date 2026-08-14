class Solution:
    def postToInfix(self , s):
        stack = []

        for char in s:
            if char.isalnum():
                stack.append(char)
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                new_expr = f"({operand1}{char}{operand2})"
                stack.append(new_expr)

        return stack[-1]


sol = Solution()
expr = "AB-DE+F*/"
print(sol.postToInfix(expr))