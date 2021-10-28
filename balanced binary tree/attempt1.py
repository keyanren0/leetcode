# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        #recursion from bottom up
        #return value [is balanced, height of this subtree]
        #return type [boolean, int]
        def bottomUp(root):
            #if it's a empty tree, return true directly
            
            if not root : return [True, 0]
            
            
            #recurse case
            left = bottomUp(root.left)
            if left[0] == False : return [False, 0]
            right = bottomUp(root.right)
            if right[0] == False : return [False, 0]
            #determine if this subtree is balanced 
            
            isBal = abs(left[1] - right[1]) <= 1
            
            return [isBal, 1 + max(left[1] , right[1])]
        return bottomUp(root)[0]
            
            