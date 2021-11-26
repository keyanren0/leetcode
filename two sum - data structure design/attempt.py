class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """

    def __init__(self):
        self.count = {}

    def add(self, number):
        # write your code here
        if number in self.count:
            self.count[number] += 1
        else:
            self.count[number] = 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        
        for number in self.count:
            if value - number in self.count and (value - number != number or self.count[number] > 1):
                return True

        return False