class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        row = [1] * n

        for _ in range(m - 1):
            for i in range(1, n):
                row[i] = row[i - 1] + row[i]

        return row[-1]