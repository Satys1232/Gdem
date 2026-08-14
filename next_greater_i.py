class Solution:
    def __init__(self):
        self.stack = []
    def next_greatest(self , s , res):
        for i in range(len(s) -1 , -1 , -1):
            ch = s[i]
            if len(self.stack) == 0:
                self.stack.append(ch)
                continue
            while self.stack and self.stack[-1] <= ch:
                self.stack.pop()
            if len(self.stack) != 0:
                res[i] = self.stack[-1]
            self.stack.append(s[i])
        return res

if __name__ == "__main__":
    s = [19 , 2 , 4 , 9 , 3 , 5 , 8 , 10]
    n = len(s)
    res = [-1] * n
    sol = Solution()
    print(sol.next_greatest(s , res))
    

            



