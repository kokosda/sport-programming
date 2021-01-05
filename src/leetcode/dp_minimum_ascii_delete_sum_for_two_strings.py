class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        res = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i == len(s1):
                    if j == len(s2):
                        continue
                    res[i][j] = ord(s2[j]) + res[i][j + 1]
                    continue
                if j == len(s2):
                    if i == len(s1):
                        continue
                    res[i][j] = ord(s1[i]) + res[i + 1][j]
                    continue
                if s1[i] == s2[j]:
                    res[i][j] = res[i + 1][j + 1]
                if s1[i] != s2[j]:
                    res[i][j] = min(ord(s1[i]) + res[i + 1][j], ord(s2[j]) + res[i][j + 1])
                    
        return res[0][0]