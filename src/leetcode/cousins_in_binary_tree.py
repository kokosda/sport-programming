# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class NodeInfo:
    def __init__(self, val: int):
        self.val = val
        self.depth = -1
        self.parent = None
    
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_info = NodeInfo(x)
        y_info = NodeInfo(y)
        
        self.dfs(root, None, 0, x_info, y_info)
        
        return x_info.depth == y_info.depth and x_info.parent is not y_info.parent
        
    def dfs(self, node: TreeNode, parent: TreeNode, cur_depth: int, x_info: NodeInfo, y_info: NodeInfo) -> None:
        if node is None:
            return

        if x_info.depth > -1 and y_info.depth > -1:
            return

        if node.val == x_info.val:
            x_info.depth = cur_depth
            x_info.parent = parent
        elif node.val == y_info.val:
            y_info.depth = cur_depth
            y_info.parent = parent

        self.dfs(node.left, node, cur_depth + 1, x_info, y_info)
        self.dfs(node.right, node, cur_depth + 1, x_info, y_info)
