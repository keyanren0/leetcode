class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        minSum = nums[0] + nums[1] + nums[-1]
        nums.sort()
        for i, x in enumerate(nums):
            
            # two pointers
            l = i+1
            r = len(nums)-1
            
            while l < r:
                tempSum = x + nums[l] + nums[r]
                
                #if sum and target have different sign , the difference needs to be add one
                if tempSum < 0 and target > 0 : tempSum -= 1
                #check if new sum is closer than temp sum, if so, pass new sum to temp
                if abs(tempSum - target) < abs(minSum - target) :
                    minSum = tempSum
                #move left pointer if the temp sum is smaller
                if tempSum - target < 0 :
                    l += 1
                #move right pointer if the temp sum is larger
                elif tempSum - target > 0:
                    r -= 1
                else :
                    return tempSum
        return minSum