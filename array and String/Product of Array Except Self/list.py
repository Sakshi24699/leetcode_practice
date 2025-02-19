nums = [1, 2, 3, 4]
n = len(nums)
res = [1] * n
lp = 1
for i in range(n):
    res[i] *= lp
    lp *= nums[i]
rp = 1
for i in range(n - 1, -1, -1):
    res[i] *= rp
    rp *= nums[i]
print(res)
