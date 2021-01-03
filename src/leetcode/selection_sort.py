class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            j_min = i
            
            for j in range(i, len(nums)):
                if nums[j_min] > nums[j]:
                    j_min = j
                
            nums[j_min], nums[i] = nums[i], nums[j_min]
            
        return nums