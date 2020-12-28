class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = self.__convert_to_graph(n, connections)
        used = [0] * n
        v0 = 0
        queue, qi = [v0], 0
        
        for edge in connections:
            while qi < len(queue):
                v = queue[qi]

                for u in graph[v]:
                    if used[u] == 0 and [v,u] != edge and [u,v] != edge:
                        queue.append(u)
                        used[u] = 1
                    
                qi += 1
        
        
    def __convert_to_graph(self, n: int, connenctions: List[List[int]]):
        res = dict()
        
        for c in connections:
            if not res.get(c[0]):
                res[c[0]] = set()
            if not res.get(c[1]):
                res[c[1]] = set()
                
            res[c[0]].add(c[1])
            res[c[1]].add(c[0])

        return res
"""
[
    [0,1],
    [1,2],
    [2,0],
    [1,3]
]
"""