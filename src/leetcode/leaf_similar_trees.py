# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node: TreeNode, seq: List[int]) -> None:
            if node is None:
                return
            
            if node.left is None and node.right is None:
                seq.append(node.val)
                return
                
            dfs(node.left, seq)
            dfs(node.right, seq)
            
        seq1 = []
        seq2 = []
        
        dfs(root1, seq1)
        dfs(root2, seq2)
        
        if len(seq1) != len(seq2):
            return False
        
        for i in range(len(seq1)):
            if seq1[i] != seq2[i]:
                return False
            
        return True