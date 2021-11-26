#import re

class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
     #   s = re.sub("[\W_]","",s).lower()
     #   
     #   return s==s[::-1]

        leftPointer = 0
        rightPointer = len(s) - 1

        while leftPointer < rightPointer:
            while leftPointer < rightPointer and not s[leftPointer].isalnum():
                leftPointer += 1
            while leftPointer < rightPointer and not s[rightPointer].isalnum():
                rightPointer -= 1
            if leftPointer < rightPointer and s[leftPointer].lower() != s[rightPointer].lower():
                return False
            leftPointer += 1
            rightPointer -= 1

        return True