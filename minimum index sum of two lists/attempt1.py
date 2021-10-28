class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        choice = []
        count = 99999999
        
        for i, m in enumerate(list1):
            if m not in list2: continue
            if count < i + list2.index(m): continue
            if count > i + list2.index(m):
                count = i + list2.index(m)
                choice.clear()
                choice.append(m)
            else :
                choice.append(m)
                
                
                
        return choice