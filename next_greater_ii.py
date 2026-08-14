class Solution:
    def __init__(self):
        self.stack = []
   
    def next_greatest(self , s , res):
        for i in range(2*len(s)-1 , -1 , -1):
            if len(self.stack) == 0:
                self.stack.append(s[i%len(s)])
                continue
            while self.stack and self.stack[-1] <= s[i%n]:
                self.stack.pop()
            if i<len(s):
                if len(self.stack) != 0:
                    res[i] = self.stack[-1]
            self.stack.append(s[i%len(s)])
        return res

if __name__ == "__main__":
    s = [19 , 2 , 4 , 9 , 3 , 5 , 8 , 10]
    n = len(s)
    res = [-1] * n
    sol = Solution()
    print(sol.next_greatest(s , res))
    

            



