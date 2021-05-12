from typing import List

class Solution:
	def get_update_days(self, rows: int, columns: int, grid: List[List[int]]) -> int:
		is_updatable = False

		for i in range(rows):
			for j in range(columns):
				if grid[i][j] == 1:
					is_updatable = True
					break

		if not is_updatable:
			return -1

		def dfs(i: int, j: int, cur_day: int, is_forced: bool=False):
			if (grid[i][j] != 0 and grid[i][j] <= cur_day) and not is_forced:
				return

			if not is_forced:
				grid[i][j] = self._get_min_surrounding(i, j, grid, cur_day)

			if i > 0:
				dfs(i - 1, j, cur_day + 1)
			if i + 1 < rows:
				dfs(i + 1, j, cur_day + 1)
			if j > 0:
				dfs(i, j - 1, cur_day + 1)
			if j + 1 < columns:
				dfs(i, j + 1, cur_day + 1)

		for i in range(rows):
			for j in range(columns):
				if grid[i][j] != 0:
					dfs(i, j, grid[i][j], is_forced=True)

		res = 0

		for i in range(rows):
			for j in range(columns):
					res = max(res, grid[i][j])

		return res - 1

	def _get_min_surrounding(self, i, j, grid, cur_day) -> int:
		tmp_day = cur_day - 1

		if i > 0 and grid[i - 1][j] != 0:
			tmp_day = min(tmp_day, grid[i - 1][j])
		if i + 1 < rows and grid[i + 1][j]:
			tmp_day = min(tmp_day, grid[i + 1][j])
		if j > 0 and grid[i][j - 1] != 0:
			tmp_day = min(tmp_day, grid[i][j - 1])
		if j + 1 < columns and grid[i][j + 1] != 0:
			tmp_day = min(tmp_day, grid[i][j + 1])

		res = tmp_day + 1
		return res

solution = Solution()

rows = 5
columns = 5
grid = [
	[1, 0, 0, 0, 0],
 	[0, 1, 0, 0, 0],
	[0, 0, 1, 0, 0],
	[0, 0, 0, 1, 0],
	[0, 0, 0, 0, 1]
]

res = solution.get_update_days(rows, columns, grid)
print(res, '\n', '\n'.join([str(row) for row in grid]), sep='')

rows = 5
columns = 6
grid = [
	[0, 0, 1, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 1],
	[0, 0, 0, 0, 0, 0],
	[0, 1, 0, 0, 0, 0]
]

res = solution.get_update_days(rows, columns, grid)
print(res, '\n', '\n'.join([str(row) for row in grid]), sep='')

rows = 5
columns = 6
grid = [
	[1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 0, 1],
	[1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1],
]

res = solution.get_update_days(rows, columns, grid)
print(res, '\n', '\n'.join([str(row) for row in grid]), sep='')

rows = 5
columns = 6
grid = [
	[1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1],
]

res = solution.get_update_days(rows, columns, grid)
print(res, '\n', '\n'.join([str(row) for row in grid]), sep='')

rows = 4
columns = 5
grid = [
	[0, 1, 1, 0, 1],
	[0, 1, 0, 1, 0],
	[0, 0, 0, 0, 1],
	[0, 1, 0, 0, 0]
 ]

res = solution.get_update_days(rows, columns, grid)
print(res, '\n', '\n'.join([str(row) for row in grid]), sep='')
