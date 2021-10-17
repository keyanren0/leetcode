class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        char = ""
        count = 0
        #set a flag to check trailing space
        flag = False
        for i in s[::-1]:
            #if there is trailing space, continue to next loop
            if i == " " and flag == False : continue
            #if there is a space and not trailing
            if i == " " : break
                
            #add num of char by 1
            count += 1
            
            #number of character starts to count, no trailing space anymore
            flag = True
        
        return count
        