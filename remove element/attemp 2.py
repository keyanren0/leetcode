class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        l = len(nums)
        while i<l:
            if nums[i] == val:
                nums[i] = nums[-1]
                nums.pop()
                l -= 1
            else: i += 1
        return l
        