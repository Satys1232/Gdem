def find_path(nums , row , col , subset , n , result , visited):
    if row == n-1 and col == n-1:
        result.append(subset.copy())
        return
    if visited[row][col] == 1:
        return
    visited[row][col] = 1
    if row + 1 < n and nums[row + 1][col] == 1: # Down
        subset.append("D")
        find_path(nums , row + 1 , col , subset , n , result , visited)
        subset.pop()
    if col - 1 >= 0 and nums[row][col-1] == 1: # Left
        subset.append("L")
        find_path(nums , row , col-1 , subset , n , result , visited)
        subset.pop()
    if col + 1 < n and nums[row][col + 1 ] == 1:
        subset.append("R")
        find_path(nums , row , col + 1 , subset , n , result , visited)
    if row - 1 >= 0 and nums[row-1][col] == 1:
        subset.append("U")
        find_path(nums , row-1 , col , subset , n , result , visited)
        subset.pop()
    visited[row][col] = 0

def all_paths(nums):
    n = len(nums)
    visited = [[0] * n for _ in range(n)]
    result = []
    find_path(nums , 0 , 0 , [] , n , result , visited)
    return result

if __name__ == "__main__":
    nums = [ 
        [ 1  ,  1  , 0] ,
        [ 0   , 1 ,  1],
        [ 1    , 1,  1]
    ]
    paths = all_paths(nums)
    print("Valid paths:" , paths)


    
