"""
A binary tree is univalued if every node in the tree has the same value.
Return true if and only if the given tree is univalued.

Example 1:
  Input: [1,1,1,1,1,null,1]
  Output: true
Example 2:
  Input: [2,2,2,5,2]
  Output: false
  
Note:
  The number of nodes in the given tree will be in the range [1, 100].
  Each node's value will be an integer in the range [0, 99].
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        my_queue = []
        list_node = []
        node = root
        my_queue.append(node)
        while my_queue:
            node = my_queue.pop(0)
            list_node.append(node.val)
            if node.left != None:
                my_queue.append(node.left)
            if node.right != None:
                my_queue.append(node.right)
        if len(set(list_node)) <= 1:
            return True
        else:
            return False
