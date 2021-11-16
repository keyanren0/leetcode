class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        large_pos = []
        i = 0
        # the index will be change during loop, thus use while not for loop
        while i < len(s)-2:
            count = 1
            flag = False
            end = 1
            #inner loop to check if is same numer in a raw
            while not flag :
                if s[i+end] == s[i] : 
                    end += 1
                    count += 1
                    
                    #if the index reach the end of string, turn the flag to prevent out of range
                    if i >= len(s) - end: flag = True
                else : flag = True
            
            if count >= 3 :
                large_pos.append([i,i+count-1])
            #move the index pointer to next
            i += end
        
        return large_pos