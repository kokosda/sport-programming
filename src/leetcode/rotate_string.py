class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B:
            return True
        
        dq = deque(A)
        counter = len(A)
        
        while counter > 0:
            ch = dq.popleft()
            
            if ch != B[0]:
                dq.append(ch)
            else:
                dq.appendleft(ch)
                
                for i in range(len(dq)):
                    if dq[i] != B[i]:
                        dq.popleft()
                        dq.append(ch)
                        break
                else:
                    return True
                
            counter -= 1
            
        return False
    
"""
"bbbacddceeb"
"ceebbbbacdd"
""
""
"a"
"a"
"a"
"b"
"abcde"
"cdeab"
"abcde"
"abced"
"""