nums = [1, 12, -5, -6, 50, 3]
k = 4

total = sum(nums[:k])
maxs = total / k
for i in range(len(nums) - k):
    total -= nums[i]
    total += nums[k + i]
    maxs = max(maxs, total / k)
print(maxs)
