class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x < 2: return x
        
        up = x // 2
        down = 2
        
        while (down <= up):
            mid = down + (up - down) // 2
            
            if mid * mid < x:
                down = mid +1
            elif mid * mid > x:
                up = mid - 1
            else:
                return math.trunc(mid)
        
        return math.trunc(up)