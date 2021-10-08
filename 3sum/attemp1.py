class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numSet = []
        nums.sort()
        for i, x in enumerate(nums):
            if i > 0 and x == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                zero = x + nums[l] + nums[r]
                if zero < 0 :
                    l += 1
                elif zero > 0:
                    r -= 1
                else :
                    numSet.append([x,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l +=1
        return numSet