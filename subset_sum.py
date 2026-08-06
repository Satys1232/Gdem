def generate_subsequence(index ,nums , result , subset , current_sum):
    if index >= len(nums):
        result.append(current_sum)
        return
    subset.append(nums[index])
    generate_subsequence(index + 1 , nums , result , subset, current_sum+nums[index])
    subset.pop()
    generate_subsequence(index + 1 , nums , result , subset, current_sum)

nums = [ 1 , 2 , 3]
result = []
current_sum = 0
generate_subsequence(0 , nums ,result , [] , current_sum)
print(result)
