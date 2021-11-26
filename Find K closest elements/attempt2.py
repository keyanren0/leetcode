class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        if not A or not k or k == 0 or k > len(A):
            return []
        ans = []
        startPoint, endPoint = 0, len(A) - 1

        while startPoint + 1 < endPoint:
            mid = startPoint + (endPoint - startPoint) // 2
            if A[mid] >= target:
                endPoint = mid
            else:
                startPoint = mid
        
        if A[startPoint] >= target:
            right = startPoint
        elif A[endPoint] >= target:
            right = endPoint
        else:
            right = len(A) - 1
        left = right - 1

        for _ in range(k):
            if self.isLeftCloser(A, target, left, right):
                ans.append(A[left])
                left -= 1
            else:
                ans.append(A[right])
                right += 1

        return ans
    
    def isLeftCloser(self, A, target, left, right):
        if left < 0:
            return False
        if right >= len(A):
            return True
        return target - A[left] <= A[right] - target



        
