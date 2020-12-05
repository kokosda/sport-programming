# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        m = len(nums) // 2
        r = TreeNode(nums[m])
        
        self.bin_assign(r, 0, m, len(nums), nums)
        
        return r
    
    def bin_assign(self, root, i, m, j, nums: List[int]):
        l = (i + m) // 2
        
        if l != m:
            print(l)
            root.left = TreeNode(nums[l])
            self.bin_assign(root.left, l, i, m, nums)
        
        r = (j + m) // 2
        
        if r != m:
            root.right = TreeNode(nums[r])
            self.bin_assign(root.right, m + 1, r, j, nums)