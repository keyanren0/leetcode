class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        if not nums or not target:
            return -1
        leftPointer, rightPointer = 0, len(nums) - 1
        
        while leftPointer + 1 < rightPointer:
            mid = leftPointer + (rightPointer - leftPointer) // 2
            if nums[mid] < target:
                leftPointer = mid
            elif nums[mid] > target:
                rightPointer = mid
            else:
                return mid

        if nums[leftPointer] == target:
            return leftPointer
        if nums[rightPointer] == target:
            return rightPointer

        return -1