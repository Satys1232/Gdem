def longest_substring(nums , maxcount , n):
    for i in range(n):
        myset = set()
        count = 0
        for j in range(n):
            if nums[j] in myset:
                break
            if nums[j] not in myset:
                myset.add(nums[j])
                count += 1
            if count > maxcount :
                maxcount = count
    return maxcount

nums = ["C" , "A" , "D" , "B" , "Z" , "X" , "A" , "B" , "C" , "D"]
n = len(nums)
print(longest_substring(nums , 0 , n ))
