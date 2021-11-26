class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        if n == 0:
            return 0
        
        row = [1] * n 


        for j in range(m):
            for i in range(n):
                if obstacleGrid[j][i] == 1:
                    row[i] = 0
                    continue 

                if i > 0 and j > 0:
                    row[i] += row[i - 1]
                    continue
                if i > 0:
                    row[i] = row[i - 1]

                print(row)
        return row[-1]

                