class Solution:
    def dayOfYear(self, date: str) -> int:
        
        month = int(date[5:7])
        day = 0
        if month == 1: return int(date[8:])
        
        for i in range(1,month):
            if i in [1,3,5,7,8,10]: day += 31
            elif i == 2:
                if (int(date[0:4]) % 400 == 0) or (int(date[0:4]) % 100 !=0 and int(date[0:4]) % 4 == 0):
                    day += 29
                else :
                    day += 28
            else:
                day += 30
        day += int(date[8:])
        
        return day