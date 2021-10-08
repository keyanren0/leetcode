class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par = { "(" : ")" , "[" : "]" , "{" : "}" }
        
        for i in s :
            if i in par:
                stack.append(i)
                
            elif not stack or par[stack.pop()] != i: return False    
                    
        return not stack