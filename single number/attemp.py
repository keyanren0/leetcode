class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        cand = 0
        
        for i in nums:
            cand ^= i
            
        return cand
                