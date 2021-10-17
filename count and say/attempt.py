class Solution:
    def countAndSay(self, n: int) -> str:
        #base case
        if n == 1:
            return "1"
        
        #recursion
        prev = self.countAndSay(n-1)
        string = ""
        count = 0
        temp = None
        for char in prev:
            # if the repeat of number is end, reset counter 
            if temp and char != temp:
                string += f"{count}{temp}"
                count = 0
            temp = char
            count += 1
        #the last set cannot be caught by recursion so need to be added
        string += f"{count}{temp}"
        return string