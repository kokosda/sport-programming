from typing import List

class Solution:
	def get_update_days(self, rows: int, columns: int, grid: List[List[int]]) -> int:
		pos_1 = None

		for i in range(rows):
			for j in range(columns):
				if grid[i][j] == 1:
					pos_1 = [i, j]
					break

		if pos_1 is None:
			return -1

		max_days = 1

		def dfs(i: int, j: int, cur_day: int):
			nonlocal max_days

			if grid[i][j] != 0:
				return

			grid[i][j] = min(\
				grid[i - 1][j] if i > -1 else 0, \
				grid[i + 1][j] if i + 1 < rows else 0, \
				grid[i][j - 1] if j -1 > -1 else 0, \
				grid[i][j + 1] + 1 if j + 1 < columns else 0)

			max_days = max(max_days, grid[i][j])

			if i - 1 > -1:
				dfs(i - 1, j, cur_day + 1)
			if i + 1 < rows:
				dfs(i + 1, j, cur_day + 1)
			if j - 1 > -1:
				dfs(i, j - 1, cur_day + 1)
			if j + 1 < columns:
				dfs(i, j + 1, cur_day + 1)

		dfs(pos_1[0], pos_1[1], 1)

		return max_days

rows = 5
columns = 6
grid = [
	[0, 0, 1, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 1],
	[0, 0, 0, 0, 0, 0],
	[0, 1, 0, 0, 0, 0]
]

solution = Solution()
res = solution.get_update_days(rows, columns, grid)
print(res, grid)