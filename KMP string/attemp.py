class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        if not target : return 0
        if not source and target : return -1

        M = len(target)
        N = len(source)

        lps_table= [0]*M

        len_of_prefix = 0
        i = 1 

        while i < M:
            if target[i] == target[len_of_prefix]:
                len_of_prefix += 1
                lps_table[i] = len_of_prefix
                i += 1

            else:
                if len_of_prefix != 0 : len_of_prefix = lps_table[len_of_prefix - 1] 

                else:
                    lps_table[i] = 0
                    i += 1
        i = 0
        j = 0
        while i < N:
            if source[i] == target[j]:
                i += 1
                j += 1
            if j == M:
                return i - M
            
            elif i < N and  source[i] != target[j]:
                if j != 0 : j = lps_table[j-1]
                else : i += 1


        return -1