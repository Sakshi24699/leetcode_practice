# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
nums1 = [1, 2, 3]
nums2 = [2, 5, 6]

m = len(nums1)
n = len(nums2)

l = m - 1
r = n - 1

while l >= 0 and r >= 0:
    if nums1[l] < nums2[r]:
        r -= 1
    else:
        nums1[l], nums2[r] = nums2[r], nums1[l]
        l -= 1
print(nums1)
print(nums2)

