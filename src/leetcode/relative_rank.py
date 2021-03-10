class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        initial_positions = dict()
        
        for i in range(len(score)):
            initial_positions[score[i]] = i
        
        score.sort(reverse=True)
        
        res = [None] * len(score)
        res[initial_positions[score[0]]] = 'Gold Medal'
        
        if len(score) > 1:
            res[initial_positions[score[1]]] = 'Silver Medal'
            
            if len(score) > 2:
                res[initial_positions[score[2]]] = 'Bronze Medal'
        
        for rank in range(3, len(score)):
            res[initial_positions[score[rank]]] = str(rank + 1)
            
        return res