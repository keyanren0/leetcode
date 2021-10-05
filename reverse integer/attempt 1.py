class Solution:
    def reverse(self, x: int) -> int:
        rever = 0
        remain = [];
        no_of_digit = 0
        if (x >= 2**31) or (x < -2**31): return 0
        if x > 0:
            while (x > 9) :
                if x > 9: remain.append(x % 10)
                else : remain.append(x % -10)
                x //= 10
                no_of_digit += 1
                
        else:
             while (x < -9):
                remain.append(x % -10)
                x = -(x // -10)
                no_of_digit += 1
        
        for num in remain:
            rever += num * (10 ** no_of_digit)
            no_of_digit -=1
            if rever >= 2**31 or rever < -2**31: return 0
            
        rever += x
        
        return rever