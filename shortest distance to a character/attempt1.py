class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        min_distance = []
        for i, n in enumerate(s):
            step = 0

            flag = False
            l = r = i
            while not flag:
                if s[l] == c or s[r] == c:
                    min_distance.append(step)
                    flag = True
                step += 1
                if l != 0: l -= 1
                if r != len(s) - 1: r += 1
                    
                    
        return min_distance