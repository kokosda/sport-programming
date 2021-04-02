class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        a_prev = A[0]
        
        for i in range(1, len(A)):
            if A[i] >= a_prev:
                a_prev = A[i]
            else:
                break
        else:
            return True
        
        a_prev = A[0]
        
        for i in range(1, len(A)):
            if A[i] <= a_prev:
                a_prev = A[i]
            else:
                break
        else:
            return True
        
        return False