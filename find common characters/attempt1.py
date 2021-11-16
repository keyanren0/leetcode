class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1 : return words[0]
        comm_char = words[0]
        
        
        for i in words[1:]:
            temp = []
            for n in comm_char:
                if n in i: 
                    temp.append(n)
                    i = i.replace(n,"!",1)  
            comm_char = temp
        return comm_char
                    