# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        memo = {}

        def dfs(root):

            if root is None:
                return 0
            
            if root in memo:
                return memo[root]

            curr_val = root.val

            if root.left:
                curr_val += dfs(root.left.left)
                curr_val += dfs(root.left.right)
            elif root.right:
                curr_val += dfs(root.right.left)
                curr_val += dfs(root.right.right)

            skip = dfs(root.left) + dfs(root.right)

            memo[root] = max(curr_val , skip)
            return memo[root]
        return dfs(root) 