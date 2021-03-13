class Solution:
	#very bad approach, needs to be reconsidered.
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        
        store = [0] * (2 * 10 ** 3 + 1)
        SHIFT = 1000
        
        for i in nums:
            store[SHIFT+i] += 1
            
        mins = self.get_candidates(0, SHIFT, 1, SHIFT, store)
        negative_maxs = self.get_candidates(len(store) // 2 - 1, -1, -1, SHIFT, store)
        maxs = self.get_candidates(len(store) - 1, SHIFT - 1, -1, SHIFT, store)
        
        if len(maxs) == 0:
            return negative_maxs[0] * negative_maxs[1] * negative_maxs[2]
        if len(maxs) == 1:
            return mins[0] * mins[1] * maxs[0]
        if len(maxs) == 2:
            if len(mins) == 1:
                return negative_maxs[0] * maxs[-1] * maxs[-2]            
            return mins[0] * mins[1] * maxs[0]
        if len(mins) >= 2:
            return max(mins[0] * mins[1] * maxs[0], maxs[0] * maxs[1] * maxs[2])
            
        return maxs[0] * maxs[1] * maxs[2]
    
    def get_candidates(self, range_from, range_to, step, shift, store):
        res = []
        
        for i in range(range_from, range_to, step):
            if store[i] is 0:
                continue
                
            tmp = store[i]
            
            while store[i] > 0:
                res.append(i - shift)
                store[i] -= 1
                
            store[i] = tmp
                
            if len(res) == 3:
                break    
                
        return res
    
"""
[-50,-50,-40,-3,0,1,4,5]
[10, 20, 1, 0, -100,-300,-20]
[1,2,3]
[-1,-2,-3]
[-100,-40,-5,-2,-1]
[-100,-40,-2,-1,1]
[-100,-40,-2,-1,1,3]
[-10,-2,-1,2]
"""