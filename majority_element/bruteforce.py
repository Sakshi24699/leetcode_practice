nums=[2,2,1,1,1,2,2]
n = len(nums)
for i in range(n):
    cnt = 0
    for j in range(n):
        if nums[j] == nums[i]:
            cnt += 1
    if cnt > (n // 2):
        print(nums[i])
        break

