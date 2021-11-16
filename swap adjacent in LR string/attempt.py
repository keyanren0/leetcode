class Solution:
    """
    @param start: the start
    @param end: the end
    @return: is there exists a sequence of moves to transform one string to the other
    """
    def canTransform(self, start, end):
        # Write your code here
        #input validation
        if len(start) != len(end):
            return False

        #extract L and R from original string
        start_set = [(start_index, start_value) for start_index, start_value in enumerate(start) if start_value != "X"]
        end_set = [(end_index, end_value) for end_index, end_value in enumerate(end) if end_value != "X"]

        #if the number of LR is not equal in two string
        if len(start_set) != len(end_set):
            return False

        # Rules: L cannot move right, R cannot move left, R and L cannot switch position
        # thus, the sequence of start_set and end_set must be equal
        # the index of L in start cannot be less than end in orginal string, reverse for R
        for i in range(len(start_set)):
            if start_set[i][1] != end_set[i][1]:
                return False
            if start_set[i][1] == "L" and start_set[i][0] < end_set[i][0]:
                return False
            if start_set[i][1] == "R" and start_set[i][0] > end_set[i][0]:
                return False

        return True