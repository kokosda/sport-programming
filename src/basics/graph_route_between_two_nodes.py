from typing import List, Deque

class Solution:
	def run(self, adj_m: List[List[int]], v1: int, v2: int) -> bool:
		v1_t = v1 - 1
		v2_t = v2 - 1
		visited_v = [False] * (len(adj_m))
		queue = Deque()
		visited_v[v1_t] = True
		self.add_to_queue(queue, adj_m, v1_t, visited_v)

		while len(queue) > 0 and visited_v[v2_t] == False:
			cur_v = queue.popleft()
			visited_v[cur_v] = True
			self.add_to_queue(queue, adj_m, cur_v, visited_v)

		res = visited_v[v2_t]
		return res

	def add_to_queue(self, queue: Deque, adj_m: List[List[int]], source_v: int, visited_v: List[int]) -> None:
		for vi in range(len(adj_m[source_v])):
			if visited_v[vi] or vi == source_v or adj_m[source_v][vi] == 0:
				continue

			queue.append(vi)

adjacency_matrix_str = """
0, 0, 0, 0, 0, 1, 0, 
0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 1, 0, 0, 0, 
0, 1, 0, 0, 1, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 
0, 0, 1, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 
"""

adj_m = [list(map(int, row[:-2].split(','))) for row in adjacency_matrix_str[1:-1].split('\n')]
solution = Solution()
is_there_a_route = solution.run(adj_m, 6, 2)
print(is_there_a_route)