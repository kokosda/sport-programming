class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        n, m = len(nums), len(nums[0])
        
        if n * m != r * c:
            return nums
        
        ni, mi = 0, 0
        res = []
        
        for ri in range(r):
            res.append([0] * c)
            
            for ci in range(c):
                if mi == m:
                    mi = 0
                    ni += 1
                    
                res[ri][ci] = nums[ni][mi]                
                mi += 1
                
        return res