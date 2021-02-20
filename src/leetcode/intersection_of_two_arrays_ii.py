class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l, g = None, None
        
        if len(nums1) < len(nums2):
            l, g = nums1, nums2
        else:
            l, g = nums2, nums1
            
        d = {}
        
        for i in l:
            if not d.get(i):
                d[i] = 1
            else:
                d[i] += 1
                
        res = []
        
        for i in g:
            count = d.get(i)
            
            if count != None and count > 0:
                res.append(i)                
                d[i] -= 1
                
        return res