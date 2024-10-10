from collections import Counter
nums = [2,2,1,1,1,2,2]
n = len(nums)
counter = Counter(nums)
for num, count in counter.items():
    if count > (n // 2):
        print(num)
