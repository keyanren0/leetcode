class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tempMap = {}
        for i,n in enumerate(nums):
            if (target - n) in tempMap: return [tempMap[target-n], i] 
            tempMap[n] = i