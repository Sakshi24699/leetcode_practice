class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=set()
        for i in range(len(nums)):
            s.add(nums[i])
        k=len(s)
        j=0
        for x in s:
            nums[j]=x
            j+=1
        return k