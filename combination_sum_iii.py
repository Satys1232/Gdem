def generate_seqeuence(index , subset , total , result , nums, n , k):
    if len(subset) == k:
        if total == n:
            result.append(subset.copy())
            return
        return
    if total > n :
        return
    if index >= len(nums):
        return
    subset.append(nums[index])
    total += nums[index]
    generate_seqeuence(index + 1 , subset , total , result , nums , n , k)
    subset.pop()
    total-= nums[index]
    generate_seqeuence(index + 1 , subset , total , result , nums , n , k)


index = 0 
subset = []
total = 0
result = []
n = 10
k = 4
nums = list(range(1 , n+1))
generate_seqeuence(index , subset , total , result , nums , n , k)
print(result)

