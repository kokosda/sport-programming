from typing import Deque, List

class Solution:
	def run(self, graph: List[List[int]]) -> None:
		queue = Deque()
		start_v_i = 0
		visited_vertices = [False] * len(graph)
		visited_vertices[start_v_i] = True
		vertices_for_queue = Solution.get_vertices_for_queue(graph, visited_vertices, start_v_i)
		Solution.append_vertices_to_queue(queue, vertices_for_queue)
		print(start_v_i + 1)

		while len(queue) > 0:
			v_i = queue.popleft()

			if not visited_vertices[v_i]:
				print(v_i + 1)
			else:
				continue

			visited_vertices[v_i] = True
			vertices_for_queue = Solution.get_vertices_for_queue(graph, visited_vertices, v_i)
			Solution.append_vertices_to_queue(queue, vertices_for_queue)

	def get_vertices_for_queue(graph: List[List[int]], visited_vertices: List[bool], v_i: int) -> List[int]:
		res = []

		for j in range(len(graph[v_i])):
			if visited_vertices[j] or i == j:
				continue

			if graph[v_i][j] != 0:
				res.append(j)

		return res

	def append_vertices_to_queue(queue, vertices_for_queue: List[int]) -> None:
		for v in vertices_for_queue:
			queue.append(v)

adjacency_matrix_str = """
0, 1, 0, 1, 0, 0
1, 0, 0, 1, 1, 1
0, 0, 0, 0, 1, 0
1, 1, 0, 0, 0, 0
0, 1, 1, 0, 0, 0
0, 1, 0, 0, 0, 0
""".split("\n")

adjacency_matrix = []

for i in range(1, len(adjacency_matrix_str) - 1):
	adjacency_matrix.append([])
	for ch in adjacency_matrix_str[i].split(", "):
		adjacency_matrix[i - 1].append(int(ch))

solution = Solution()
solution.run(adjacency_matrix)