class Solution:

    def __init__(self):
        self.stack = []

    def remaining_asterioids(self , nums):
        for char in nums:
            if len(self.stack) == 0:
                self.stack.append(char)
                continue
            if self.stack and self.stack[-1] > 0 and char < 0:
                while self.stack and -char > self.stack[-1] and self.stack[-1] > 0:
                    self.stack.pop()
                if not self.stack or self.stack[-1] < 0 :
                    self.stack.append(char)
                elif self.stack[-1] == -char:
                    self.stack.pop()
                continue 
            self.stack.append(char)
        return self.stack
if __name__ == "__main__":
    nums = [4 , 7 , 1 , 1 , 2 , -3 , -7 , 17 , 15 , -18 , -19]
    sol = Solution()
    print(sol.remaining_asterioids(nums))

                    
            