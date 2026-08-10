class Solution:
    def isSafe(self, row , col , board , n):
        duplrow = row
        duplcol = col
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1
        col = duplcol
        row = duplrow
        while col >= 0:
            if board[row][col] == "Q":
                return False
            col -= 1
        col = duplcol
        row = duplrow
        while row < n and col >= 0 :
            if board[row][col] == "Q":
                return False
            row += 1
            col -= 1
        return True
    def solve(self , col , board , ans , n):
        if col == n:
            ans.append(list(board))
            return
        for row in range (n):
            if self.isSafe(row , col , board , n):
                board[row] = board[row][:col] + "Q" + board[row][col+1:]
                self.solve(col+1 , board , ans , n)
                board[row] = board[row][:col] + "." + board[row][col+1:]
        return

if __name__ == "__main__":
    ans = []
    n = 4
    board = ["." * n for _ in range(n)]
    col = 0 
    sol = Solution()
    sol.solve(0 , board , ans , n)
    for one_solution in ans:
        for row in one_solution:
            print(" ".join(row))
        print()
