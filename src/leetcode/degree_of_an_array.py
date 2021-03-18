class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq_store = dict()
        
        for i in range(len(nums)):
            num = nums[i]
            
            if freq_store.get(num) is None:
                freq_store[num] = [i, i, 1]
            else:
                freq_store[num][1] = i
                freq_store[num][2] += 1
            
        degree = 0
        
        for k in freq_store:
            degree = max(degree, freq_store[k][2])
            
        res = len(nums)

        for k in freq_store:
            v = freq_store[k]
            
            if v[2] != degree:
                continue
            
            res = min(res, v[1] - v[0] + 1)
            
        return res
    
"""
4,0,4,4,2,2,6,1,2
"""