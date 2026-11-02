# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        
        left_depth = 0
        left_node = root
        while left_node:
            left_depth += 1
            left_node = left_node.left

        
        right_depth = 0
        right_node = root
        while right_node:
            right_depth += 1
            right_node = right_node.right

        
        if left_depth == right_depth:
            return (1 << left_depth) - 1

       
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)