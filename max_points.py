def max_points(nums = [1 , 2 , 3 , 4 , 5 , 6 , 1], k = 3):
    n = len(nums)
    if n == k:
        return sum(nums)
    left_sum = sum(nums[:k])
    right_sum = 0 
    maxi = left_sum
    right_ind = n-1
    for i in range(k-1,-1,-1):
        left_sum -= nums[i]
        right_sum += nums[right_ind]
        maxi = max(maxi,left_sum + right_sum)
        right_ind-=1
    return maxi
print(max_points())