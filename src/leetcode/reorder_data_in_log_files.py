class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        ld = dict()
        
        for log in logs:
            split_log = log.split(' ', 1)
            
            if split_log[1][0].isdigit():
                digits.append(log)
            else:
                letters.append(log)
                ld[log] = ld.get(log, (split_log[1], split_log[0]))
                
        letters.sort(key=lambda x: ld[x])
        
        res = [*letters, *digits]
        return res
        
"""
1 art can
2 art zero
3 can art
4 can bar
"""