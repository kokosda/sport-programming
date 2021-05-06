#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        
        def dfs(node: TreeNode) -> None:
            if node is None:
                return
            
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
            
        dfs(root)
        
        def build_tree(node: TreeNode, s: int, e: int) -> TreeNode:
            if s == e:
                return

            mid = (s + e) // 2
            
            if node is None:
                balanced_root = TreeNode(arr[mid])                
                build_tree(balanced_root, s, mid)
                build_tree(balanced_root, mid + 1, e)
                return balanced_root
            else:
                if arr[mid] < node.val:
                    node.left = TreeNode(arr[mid])
                    build_tree(node.left, s, mid)
                    build_tree(node.left, mid + 1, e)
                    return node.left
                else:
                    node.right = TreeNode(arr[mid])
                    build_tree(node.right, s, mid)
                    build_tree(node.right, mid + 1, e)
                    return node.right
                    
        res = build_tree(None, 0, len(arr) - 1)
        return res
        
"""
[1,null,2,null,3,null,4,null,null]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                     5
            3                    8
        2        4           7       9
    1                    6             10
"""

root = \
TreeNode(1, None, \
    TreeNode(2, None, \
        TreeNode(3, None, \
            TreeNode(4, None, \
                TreeNode(5, None, \
                    TreeNode(6, None, \
                        TreeNode(7, None, \
                            TreeNode(8, None, \
                                TreeNode(9, None, \
                                    TreeNode(10, None, None))))))))))

solution = Solution()
res = solution.balanceBST(root)

print(res)