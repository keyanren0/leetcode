class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum =temp_sum= sum(nums[:k])
    
        for i in range(len(nums)-k):
            temp_sum += (nums[i+k] - nums[i])
            max_sum = max(max_sum, temp_sum)
        return max_sum / k