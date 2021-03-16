class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if len(moves) % 2 is not 0:
            return False
        
        kinds = {ch:0 for ch in 'UDRL'}
        
        for m in moves:
            kinds[m] += 1
            
        return kinds['U'] == kinds['D'] and kinds['L'] == kinds['R']