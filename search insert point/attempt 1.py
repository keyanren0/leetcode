class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # treat edge case first for saveing time
        
        if target < nums[0] : return 0
        if target > nums[-1] : return len(nums) 
        
        # two pointers starts from begining and end of the list
        l,r = 0 , len(nums)-1
        
        # loop until no match element found
        while l <= r:
            mid = (l+r)//2  ## start from middle
            
            if nums[mid] == target: # if mid point is target
                return mid
            elif nums[mid] < target: # if mid is less than larget move left pointer to mid, +1 for preventing inf loop
                l = mid +1
                
            # move right pointer if something else
            else:
                r = mid-1
                
        return l