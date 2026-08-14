class ValidParantheses:
    def __init__(self):
        self.stack = []
    def invalid(self , s:str) -> bool:
        for bracket in s:
            if bracket == "(" or bracket == "[" or bracket == "{":
                self.stack.append(bracket)
            else:
                if len(self.stack) == 0:
                    return False
                ch = self.stack.pop()
                if ((bracket == ")" and ch == "(") or (bracket == "]" and ch == "[") or (bracket == "}" and ch == "{")):
                    continue
                else:
                    return False
        return len(self.stack) == 0

check = ValidParantheses()
print(check.invalid("((()))"))
