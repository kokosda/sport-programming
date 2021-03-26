class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        sq = self._get_dq(S)
        tq = self._get_dq(T)
        
        if len(sq) != len(tq):
            return False
        
        for i in range(len(sq)):
            if sq[i] != tq[i]:
                return False
            
        return True
            
    def _get_dq(self, src: str) -> deque[str]:
        res = deque()
        
        for i in range(len(src)):
            if src[i] is '#':
                if res:
                    res.pop()
            else:
                res.append(src[i])
                
        return res
        
    def backspaceCompare_cycle(self, S: str, T: str) -> bool:
        i = len(S) - 1
        j = len(T) - 1
        
        while i >= 0 or j >= 0:
            i = self._get_pos(S, i)
            j = self._get_pos(T, j)
            
            if i > -1 and j > -1 and S[i] == S[j]:
                i -= 1
                j -= 1
            
            
            print(i, j)
            
            if i > -1 and j > -1:
                if S[i] == S[j]:
                    i -= 1
                    j -= 1
                else:
                    return False
                
            
        
        print(i, j)
        return i == j
    
    def _get_pos(self, src: str, idx: int):
        acc = 0
        
        while idx >= 0:
            if src[idx] is '#':
                acc += 1
            elif acc > 0:
                acc -= 1
            else:
                return idx
            
            idx -= 1
            
        return -1
            
                
"""
"aa##a#a#"
        ^
"aa##a###b"
    ^
"a"

"ab#c"
"ad#c"

"nzp#o#g"
"b#nzp#o#g"
"xywrrmp"
"xywrrmu#p"
"aa##a#a#"
"aa##a###"
"aa##a#a#"
"aa##a###b"
"ab#c"
"ad#c"
"ab#c"
"ad#c"
"ab##"
"c#d#"
"a##c"
"#a#c"
"a#c"
"b"
"""            