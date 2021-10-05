class Solution:
    def reverse(self, x: int) -> int:
        rever = 0
        if (x >= 2**31) or (x < -2**31): return 0
        if x > 0:
            while (x != 0) :
                remain = x % 10
                x //= 10
                rever = rever * 10 + remain
                if rever >= 2**31 or rever < -2**31: return 0
                
        else:
             while (x != 0):
                remain = x % -10
                x = -(x // -10)
                rever = rever * 10 + remain
                if rever >= 2**31 or rever < -2**31: return 0
            
        
        return rever