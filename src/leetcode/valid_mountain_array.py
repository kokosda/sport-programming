class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        start_i = 0
        prev_i = 0
        i = 1
        
        while i < len(arr) and arr[i] > arr[prev_i]:
            prev_i = i
            i += 1
            
        if i == len(arr) or start_i == prev_i or arr[i] == arr[prev_i]:
            return False
        
        start_i = prev_i
        
        while i < len(arr) and arr[i] < arr[prev_i]:
            prev_i = i
            i += 1
        
        return prev_i != start_i and i == len(arr)