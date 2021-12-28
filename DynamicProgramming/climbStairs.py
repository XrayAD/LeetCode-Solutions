class Solution:  # O(n) space, but possible to only use two pointers from before
    def climbStairs(self, n: int) -> int:
        rec = [1] * (n+1)
        for i in range(2,n+1):
            rec[i] = rec[i-2] + rec[i-1]
        return rec[-1]


class Solution2:
    def climbStairs(self, n: int) -> int:
        prev1 = 1
        prev2 = 1
        if n == 1:
            return 1
        for i in range(2,n+1):
            tmp = prev1
            prev1 = prev1 + prev2
            prev2 = temp
        return prev1
