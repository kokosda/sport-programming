class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = dict()
        
        for i in range(len(nums2)):
            d[nums2[i]] = -1
            
            for j in range(i + 1, len(nums2)):
                if nums2[i] < nums2[j]:
                    d[nums2[i]] = nums2[j]
                    break
                
        res = [d[num] for num in nums1]
        return res