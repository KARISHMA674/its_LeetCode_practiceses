# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_len = 0

        def dfs(node, go_left, steps):
            if not node:
                return
            
            self.max_len = max(self.max_len, steps)

            if go_left:
                dfs(node.left, False, steps + 1)
                dfs(node.right, True, 1)
            else:
                dfs(node.right, True, steps + 1)
          
                dfs(node.left, False, 1)

        
        dfs(root.left, False, 1)
        dfs(root.right, True, 1)

        return self.max_len
        