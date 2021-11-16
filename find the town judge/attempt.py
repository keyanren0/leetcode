class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustto = [0] * n
        trusted = [0] * n
        #count the number of trust and trusted for each individual 
        for i in trust:
            trustto[i[0]-1] +=1
            trusted[i[1]-1] +=1
            
        #if the person is judge, the count of trust should be 0 and trusted should be n-1
        for i in range(n):
            if trustto[i] == 0 and trusted[i] == n-1:
                return i+1
        
        return -1
            
        
        
        