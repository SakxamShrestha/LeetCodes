'''
U: Just changing the position of a binary tree. Doesnt need to be a binary search Tree. 
M:
Initial thought is to change all the leaf nodes as well as the body nodes except the main root node. Just flip them. 
Btw we have to use recursion in this question to recursively go through each node of the tree and flip it. 
Starter codes are to be given, but if not, it is simple. 
self.val = val
self.right = right
self.let = left
P
I
R
E
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: # If there is no root, i mean the first root node, no need to do anything just return None. You can ask the interviewer though cause this is like an edge case. 
            return None
    
    # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # Swap the left and right children, just like you changed / incremented two pointers, use comma for impactful code. 
        root.left, root.right = root.right, root.left
        
        return root # after we recursively go through every node of this binary tree, finally we can return the node. 
        
