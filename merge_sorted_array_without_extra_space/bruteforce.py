nums1 = [1, 2, 3]
nums2 = [2, 5, 6]

m = len(nums1)
n = len(nums2)

l = 0
r = 0
nums3 = []
while l < m and r < n:
    if nums1[l] < nums2[r]:
        nums3.append(nums1[l])
        l += 1
    else:
        nums3.append(nums2[r])
        r += 1
while r < n:
    nums3.append(nums2[r])
    r += 1
while l < m:
    nums3.append(nums1[l])
    l += 1

print(nums3)
