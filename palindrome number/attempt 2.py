class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0 : return True
        if x < 0  : return False
        if x % 10 == 0 : return False
        rever = 0
        while (x > rever) :
                remain = x % 10
                x //= 10
                rever = rever * 10 + remain
            #    if rever >= 2**31 : return 0
                
        if rever == x or x == rever // 10: return True
        else : return False