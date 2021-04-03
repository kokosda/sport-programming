class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        dq = deque()
        
        for i in A:
            if i % 2 is 0:
                dq.appendleft(i)
            else:
                dq.append(i)
                
        return dq