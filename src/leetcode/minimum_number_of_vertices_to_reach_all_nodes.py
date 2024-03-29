class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        store = set([i for i in range(n)])
        
        for e in edges:
            if e[1] in store:
                store.remove(e[1])
            
        res = list(store)
        return res
    
    def findSmallestSetOfVertices_list(self, n: int, edges: List[List[int]]) -> List[int]:
        store = [i for i in range(n)]
        
        for e in edges:
            store[e[1]] = -1
            
        res = [i for i in range(n) if store[i] is not -1]
        return res
        