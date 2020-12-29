class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        ht = self.__convert_to_hash_table(n, connections)
        res = []
        
        for edge in connections:
            used = [0] * n
            used[0] = 1
            used_assignments = 1
            v0, v = 0, None
            queue, qi = [v0], 0
            
            while qi < len(queue):
                v = queue[qi]

                for u in ht[v]:
                    if used[u] == 0:
                        if not self.__is_vu_in_edge(v, u, edge):
                            queue.append(u)
                            used[u] = 1
                            used_assignments += 1
                    
                qi += 1
                
            if used_assignments < n:
                res.append(edge)

        return res
        
    def __convert_to_hash_table(self, n: int, connections: List[List[int]]):
        res = dict()
        
        for c in connections:
            if not res.get(c[0]):
                res[c[0]] = set()
            if not res.get(c[1]):
                res[c[1]] = set()
                
            res[c[0]].add(c[1])
            res[c[1]].add(c[0])

        return res
    
    def __is_vu_in_edge(self, v: int, u: int, edge: List[int]) -> bool:
        return (edge[0] == v or edge[1] == v) and (edge[0] == u or edge[1] == u)
    
"""
{0: {1,2}}
{1: {0,2,3}}
{2: {0,1,5}}
{3: {1,4}}
{4: {3}}
{5: {2}}

6
[[0,1],[0,2],[1,2],[1,3],[2,5],[3,4]]
"""