def generate_subsequence(index , subset , result , nums , sum_nums):
    if index >= len(nums):
        result.append(sum_nums)
        return
    subset.append(nums[index])
    generate_subsequence(index + 1 , subset , result , nums , sum_nums+ nums[index])
    subset.pop()
    generate_subsequence(index + 1 , subset , result , nums , sum_nums)

index = 0 
subset = []
result = []
nums = [1 , 2 , 3]
sum_nums = 0
generate_subsequence(index , subset , result , nums , sum_nums)
print(result)
