class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = 0
        for n in nums:
            if n != val: 
                nums[a] = n
                a += 1
        return a
        