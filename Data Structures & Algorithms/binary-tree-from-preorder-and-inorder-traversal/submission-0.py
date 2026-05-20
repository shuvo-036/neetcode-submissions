# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mapp ={}
        for i in range(len(inorder)):
            mapp[inorder[i]] =i
        preorder = deque(preorder)
        def dfs(start,end):
            if start > end:
                return 
            
            root_val = preorder.popleft()
            root = TreeNode(root_val)
            mid = mapp[root_val]
            root.left = dfs(start, mid -1)
            root.right = dfs(mid+1 ,end)
            return root
        return dfs(0, len(inorder)-1)