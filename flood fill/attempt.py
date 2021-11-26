class Solution:
    """
    @param image: a 2-D array
    @param sr: an integer
    @param sc: an integer
    @param newColor: an integer
    @return: the modified image
    """
    def dfs(self, image, x, y, color, newColor):
        if x < 0 or y < 0 or x >= len(image) or y >= len(image[0]) or image[x][y] != color:
            return
        image[x][y] = newColor
        self.dfs(image, x + 1, y, color, newColor)
        self.dfs(image, x - 1, y, color, newColor)
        self.dfs(image, x, y + 1, color, newColor)
        self.dfs(image, x, y - 1, color, newColor)

    def floodFill(self, image, sr, sc, newColor):
        # Write your code here
        if image[sr][sc] == newColor:
            return image
        self.dfs(image, sr, sc, image[sr][sc], newColor)

        return image