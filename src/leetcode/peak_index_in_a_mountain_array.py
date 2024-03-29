class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        s = 0
        e = len(arr)
        
        while True:
            m = (s + e) // 2
            
            if arr[m - 1] < arr[m] > arr[m + 1]:
                return m

            if arr[m - 1] < arr[m] < arr[m + 1]:
                s = m + 1
            else:
                e = m