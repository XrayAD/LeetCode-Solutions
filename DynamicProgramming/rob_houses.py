from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        found = [None]*len(nums)
        def recurse(nums, i: int):
            if i >= len(nums):
                return 0
            elif i == len(nums) - 1:
                return nums[i]
            else:
                if found[i] is not None:
                    return found[i]
                found[i] = max(nums[i] + recurse(nums,i+2), recurse(nums, i+1))
                return found[i]
        return recurse(nums, 0)

a = Solution()
print(a.rob([2,7,9,3,1]))
