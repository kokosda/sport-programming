class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums_len = len(nums) + 2
        max_points = [[0] * nums_len for _ in range(nums_len)]
        
        for length in range(nums_len):
            for l in range(nums_len - length):
                r = l + length
                print(f'len={length}, l={l}, r={r}, j={None}')
                for j in range(l + 1, r):
                    print(f'len={length}, l={l}, r={r}, j={j}')
                    nums_l = nums[l] if l < nums_len - 2 else 1
                    nums_j = nums[j] if j < nums_len - 2 else 1
                    nums_r = nums[r] if r < nums_len - 2 else 1
                    max_points[l][r] = max_points[l][j] + max_points[j][r] + nums_l * nums_j * nums_r
        
        for mp in max_points:
            print(mp)
        return max_points[0][nums_len - 1]