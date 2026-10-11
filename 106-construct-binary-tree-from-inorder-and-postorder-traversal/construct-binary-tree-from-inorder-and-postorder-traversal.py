# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        
        inorder_idx_map = {val: i for i, val in enumerate(inorder)}
        
        def helper(left_in, right_in):
            
            if left_in > right_in:
                return None
            
            root_val = postorder.pop()
            root = TreeNode(root_val)
            
            
            mid = inorder_idx_map[root_val]
            
            
            root.right = helper(mid + 1, right_in)
            root.left = helper(left_in, mid - 1)
            
            return root
        
        return helper(0, len(inorder) - 1)