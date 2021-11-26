class Solution:
    """
    @param s: a string
    @return: a string
    """
    def largestLetter(self, s):
        if not s:
            return "NO"
        lowerChar = []
        upperChar = []

        for char in s:
            if char.islower():
                lowerChar.append(char)
                continue
            upperChar.append(char)
        largestChar = []
        for char in lowerChar:
            if char.upper() in upperChar:
                largestChar.append(ord(char))
        if largestChar:
            return chr(max(largestChar)).upper()

        return "NO"