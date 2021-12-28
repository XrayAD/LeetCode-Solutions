from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        saved_sums = triangle[-1]
        for row in triangle[-2::-1]:
            for i in range(len(row)):
                saved_sums[i] = row[i] + min(saved_sums[i], saved_sums[i+1])
        return saved_sums[0]

a = Solution()
print(a.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
