class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        #create a blank triangle with full of 1
        pascal = [[1] * i for i in range(1,numRows+1)] 
        
        #start from row 3, overwrite the value to desired
        for row in range(2, len(pascal)):
            
            #from the second one in column to second last
            
            for col in range(1, len(pascal[row])-1):
                
                # each cell is sum of the one before it and same as it in index in previous row
                pascal[row][col] = pascal[row-1][col-1] + pascal[row-1][col]

        return pascal