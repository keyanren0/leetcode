class Solution:
    def romanToInt(self, s: str) -> int:
        codex = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        current = 0
        previous = 0
        for r in s[::-1]:
            if codex[r] >= previous:
                current += codex[r]
            else:
                current -= codex[r]
            previous = codex[r]
        return current