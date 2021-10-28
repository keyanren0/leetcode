class Solution:
    def reverseBits(self, n: int) -> int:
        re = 0
        
        for i in range(31):
            re = re ^ (n % 2)
            re <<= 1
            n >>= 1
        re = re ^ (n % 2)
        return re