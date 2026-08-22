def find_max(mydict , left , right , maxi , nums , n):
    while right < n:
        if nums[right] in mydict:
            left = max(left , mydict[nums[right]]+1)
        maxi = max(maxi , right-left+1) 
        mydict[nums[right]] = right
        right += 1
    return maxi

if __name__ == "__main__":
    mydict = {}
    left  = 0
    right = 0
    maxi = 0
    nums = ["C" , "A" , "D" , "B" , "Z" , "A" , "B" , "C" , "D"]
    n = len(nums)
    print(find_max(mydict, left , right , maxi , nums , n))