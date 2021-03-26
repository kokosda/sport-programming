class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = dict()
        
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
            
        longest_seq = 0
        
        for k in freq:
            if freq.get(k + 1):
                longest_seq = max(longest_seq, freq[k] + freq.get(k + 1))
            
        return longest_seq