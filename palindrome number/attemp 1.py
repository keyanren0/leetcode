class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0 : return True
        if x < 0 or x % 10 == 0 : return False
        
        rever = 0
        temp = x
        while (x != 0) :
                remain = x % 10
                x //= 10
                rever = rever * 10 + remain
                if rever >= 2**31 : return 0
                
        if rever == temp: return True
        else : return False