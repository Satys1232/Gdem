def max_ones(nums , k):
    maxi = 0 
    left = 0 
    right = 0 
    zeroes = 0 
    n = len(nums)
    while right < n:
        if nums[right] == 0:
            zeroes += 1
        if zeroes > k:
            if nums[left] == 0:
                zeroes -= 1
            lefkt += 1
        if zeroes <= k:
            maxi = max(maxi , right-left+1)
        right += 1
    return maxi

nums = [ 1 , 1 , 1, 0 , 0 , 0 , 1 , 1, 1 , 1, 1]
k = 2
print(max_ones(nums ,k))