class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l, g = None, None
        
        if len(nums1) < len(nums2):
            l, g = nums1, nums2
        else:
            l, g = nums2, nums1
        
        ls, gs = set(), set()
        
        for i in l:
            ls.add(i)
            
        for i in g:
            gs.add(i)
        
        res = []
        
        for i in ls:
            if i in gs:
                res.append(i)
        
        return res
    
    def intersection_sets(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set(nums1).intersection(set(nums2))
        return list(res)
    
"""
[2,2,1]
[1,2,2,1,3]
"""