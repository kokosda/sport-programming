from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = set()

        p1 = 0

        while p1 < len(rating) - 2:
            p2 = self.get_next_larger(rating, p1)

            while p2 != -1 and p2 < len(rating) - 1:
                p3 = p2

                while p3 != -1 and p3 < len(rating):
                    p3 = self.get_next_larger(rating, p2, from_pos=p3)

                    if p3 > -1:
                        res.add(f'{p1}-{p2}-{p3}')

                p2 = self.get_next_larger(rating, p1, from_pos=p2)

            p1 += 1

        p1 = len(rating) - 1

        while p1 >= 2:
            p2 = self.get_next_smaller(rating, p1)

            while p2 >= 1:
                p3 = p2

                while p3 >= 0:
                    p3 = self.get_next_smaller(rating, p2, from_pos=p3)

                    if p3 > -1:
                        res.add(f'{p3}-{p2}-{p1}')

                p2 = self.get_next_smaller(rating, p1, from_pos=p2)

            p1 -= 1

        return len(res)

    def get_next_larger(self, rating, pos, from_pos=None) -> int:
        i = from_pos + 1 if from_pos is not None else pos + 1

        while i < len(rating):
            if rating[i] > rating[pos]:
                return i

            i += 1

        return -1

    def get_next_smaller(self, rating, pos, from_pos=None) -> int:
        i = from_pos - 1 if from_pos is not None else pos - 1

        while i >= 0:
            if rating[i] > rating[pos]:
                return i

            i -= 1

        return -1

"""
[2,5,3,4,1,7]
 ^   ^ ^

larger:
p1: 0
p2: 2
p3: 5

[0,1,5];[0,2,3]
"""

solution = Solution()
res = solution.numTeams([2,5,3,4,1,7])
print(res)