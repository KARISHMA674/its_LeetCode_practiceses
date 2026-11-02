# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.stack = []
        self._push_all_left(root)

    def _push_all_left(self, node):
        """Helper to push the node and all of its left descendants."""
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        """
        :rtype: int
        """
        
        top_node = self.stack.pop()
        
        
        if top_node.right:
            self._push_all_left(top_node.right)
            
        return top_node.val

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0



        


