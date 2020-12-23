# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return '[]'
        
        queue = [[root, 1]]
        qi = 0
        res = []
        
        while qi < len(queue):
            cur_node, depth = queue[qi]
            
            if depth > len(res):
                res.append([])
            
            if cur_node != None:
                res[depth - 1].append(cur_node.val)
            else:
                res[depth - 1].append(None)
                
            if cur_node != None:
                queue.append([cur_node.left, depth + 1])
                queue.append([cur_node.right, depth + 1])
                
            qi += 1
            
        def linerize(jaggedArr):
            result = []
            
            for elArr in jaggedArr:
                for el in elArr:
                    result.append(el)
                    
            return result
        
        def strip_ending_nones(arr):
            i = len(arr)- 1
            
            while arr[i] == None:
                i -= 1
                
            return arr[:i + 1]
            
        res = linerize(res)
        res = strip_ending_nones(res)
        
        result = '[' + ','.join([str(i) for i in res]) + ']'        
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if data == None or data == '[]' or len(data) < 3:
            return None
        print(data)
        data_arr = [int(i) if i != 'None' else None for i in data[1:-1].split(',')]
        data_arr_ind = 1
        root = TreeNode(data_arr[0])
        queue = [root]
        qi = 0
        
        while data_arr_ind < len(data_arr):
            cur_node = queue[qi]
            val = data_arr[data_arr_ind]
            
            if val != None:
                node = TreeNode(val)
                queue.append(node)
                
                if data_arr_ind % 2 != 0:
                    cur_node.left = node
                else:
                    cur_node.right = node
                
            if data_arr_ind % 2 == 0:
                qi += 1
            
            data_arr_ind += 1
            
        return root 
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))