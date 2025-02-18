nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
ans0 = []
ans1 = []
r = [[], []]
for i in range(len(nums1)):
    if nums1[i] not in nums2 and nums1[i] not in r[0]:
        r[0].append(nums1[i])

for i in range(len(nums2)):
    if nums2[i] not in nums1 and nums2[i] not in r[1]:
        r[1].append(nums2[i])
print(r)