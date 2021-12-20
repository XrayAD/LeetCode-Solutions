from typing import List
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        d = {}
        current = 0
        total = 0
        i = 0
        while (i <= len(nums) - k):
            d.clear()
            current = 0
            p = i + k
            for j in range(i,  i+k):
                if d.get(nums[j]) is None:
                    current += 1
                    d[nums[j]] = 1
            if (current == k):
                total+=1
            while(current <= k and p < len(nums)):
                if d.get(nums[p]) is None:
                    current += 1
                    d[nums[p]] = 1
                if (current==k):
                    total+=1
                p += 1
            i += 1
        return total

a = Solution()
