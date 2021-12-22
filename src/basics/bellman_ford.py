from __future__ import annotations
from typing import List

class Constants:
	INFINITY = 10 ** 6

class Solution:
	def run(self, g: Graph, source_vertice: int, destination_vertice: int) -> bool:
		g.vertices[source_vertice].weight_upper_bound = 0
		
		for _ in g.vertices:
			for edge in g.edges:
				self.__relax__(g, edge.vertice_1, edge.vertice_2, edge.weight)
				
		for edge in g.edges:
			if edge.vertice_2.weight_upper_bound > (edge.vertice_1.weight_upper_bound + edge.weight):
				return False

		return True

	def __relax__(self, g: Graph, u: int, v: int, weight: int) -> None:
		weight_upper_bound = u.weight_upper_bound + u.edges[v].weight

		if v.weight_upper_bound > weight_upper_bound:
			v.weight_upper_bound = weight_upper_bound
			v.predecessor = u

class Vertice:
	def __init__(self, number: int):
		self.number = number
		self.weight_upper_bound = Constants.INFINITY
		self.predecessor = None
		self.edges = []

	def add_edge(self, vertice: Vertice, weight: int) -> Edge:
		result = Edge(self, vertice, weight)
		self.edges.append(result)
		return result
	
	def __str__(self) -> str:
		return f'{self.number}, wub {self.weight_upper_bound}, pred {self.predecessor}'

	def __repr__(self) -> str:
		return self.__str__()

class Edge:
	def __init__(self, vertice_1: Vertice, vertice_2: Vertice, weight: int):
		self.vertice_1 = vertice_1
		self.vertice_2 = vertice_2
		self.weight = weight

	def __str__(self) -> str:
		return f'{self.vertice_1.number} -> {self.vertice_2.number}: {self.weight}'

	def __repr__(self) -> str:
		return self.__str__()

class Graph:
	def __init__(self, serialized_adjacency_matrix: str):
		adjacency_matrix = self.__get_adjacency_matrix__(serialized_adjacency_matrix)
		self.vertices = [Vertice(i) for i in range(len(adjacency_matrix) + 1)]
		self.edges = []

		for i in range(len(adjacency_matrix)):
			number = i + 1
			vertice = self.vertices[number]

			for j in range(len(adjacency_matrix[i])):
				weight = adjacency_matrix[i][j]

				if weight == 0:
					continue

				edge = vertice.add_edge(self.vertices[j + 1], weight)
				self.edges.append(edge)

	def __get_adjacency_matrix__(self, serialized_adjacency_matrix: str) -> List[List[int]]:
		result = []

		for i in range(1, len(serialized_adjacency_matrix) - 1):
			result.append([])
			row = serialized_adjacency_matrix[i].split(", ")
			for j in range(len(row) - 1):
				result[i - 1].append(int(row[j]))
		
		return result

adjacency_matrix_str = """
0, 6, 0, 0, 7, 
0, 0, 5, -4, 8, 
0, -2, 0, 0, 0, 
2, 0, 7, 0, 0, 
0, 0, -3, 9, 0, 
""".split("\n")

graph = Graph(adjacency_matrix_str)

solution = Solution()
solution.run(graph, 1, 5)