class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = [0] * 1001
        
        for i in arr1:
            count[i] += 1
            
        res = []
        
        for i in arr2:
            res += [i] * count[i]
            count[i] = 0
            
        tail_res = []
        
        for i in arr1:
            if count[i] == 0:
                continue
                
            tail_res += [i] * count[i]
            count[i] = 0
            
        tail_res.sort()
        res = res + tail_res
        return res

"""
[2,7,2,2,0,8,1,1,1,0,5,3,3,1,3,3,0,3]
[1,0,3]
[2,2,2,2]
[2]
[2,3,1,3,2,4,6,7,9,2,19]
[2,1,4,3,9,6]
"""