nums = [1,2,3,4,5,6,7]
k=3
n=len(nums)
if (n == 0):
    print(-1)
k = k % n
if (k > n):
    print(-1)
temp=[]
for i in range(n-k):
    temp.append(nums[i])
for i in range(n-k, n):
    nums[i - n + k] = nums[i]
for i in range(k, n):
    nums[i] = temp[i-k]
print(nums)
