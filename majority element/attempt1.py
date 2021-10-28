class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        record_count = 1
        record_num = nums[0]
        temp_count = 1
        
        
        
        for i,n in enumerate(nums[1:]):
            if n == nums[i-1]: temp_count += 1
            else: temp_count = 1
            if temp_count > record_count: 
                record_count = temp_count
                record_num = n
            if record_count > len(nums)/2 : break
                
                
        return record_num