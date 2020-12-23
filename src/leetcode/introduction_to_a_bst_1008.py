# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.queue = BSTIterator.get_queue(root)
        self.queue_ind = -1

    def next(self) -> int:
        if self.hasNext():
            self.queue_ind += 1
            return self.queue[self.queue_ind]

        return None

    def hasNext(self) -> bool:
        return (self.queue_ind + 1) < len(self.queue)
        
    def get_queue(root: TreeNode) -> List[TreeNode]:
        res = []
        stack = []
        cur_node = root
        is_left_considered = True
        
        while cur_node != None:                
            if cur_node.left != None and is_left_considered:
                stack.append(cur_node)
                cur_node = cur_node.left
                continue
            
            if cur_node.right != None:
                stack.append(cur_node.right)
                is_left_considered = True
            else:
                is_left_considered = False

            res.append(cur_node.val)
                
            if len(stack) > 0:
                cur_node = stack.pop()
            else:
                cur_node = None
        
        return res


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()