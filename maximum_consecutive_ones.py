def max_ones(nums , n , k , maxi):
    for i in range(0,n):
        zeroes = 0
        for j in range(i,n):
            if nums[j] == 0:
                zeroes +=1 
            if zeroes > k:
                break
            maxi = max(maxi , j-i+1)
    return maxi

nums = [ 1 , 1 , 1 , 0 , 0 , 0 , 1 , 1 , 1 , 1  , 0]
k = 2
n = len(nums)
maxi = 0
print(max_ones(nums , n , k , maxi))
