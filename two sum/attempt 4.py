class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tempMap = {}
        for i,n in enumerate(nums):
            x = target - n
            if (x) in tempMap: return [tempMap[x], i] 
            tempMap[n] = i