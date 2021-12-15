from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if (len(nums) == 0):
            return -1
        index = int(len(nums)/2)
        start = 0
        finish = len(nums) - 1
        while (start != finish):
            print(start)
            print(finish)
            if (nums[index] == target):
                return index
            elif nums[index] > target:
                finish = index
                index = int((start + finish)/2)
            else:
                start = index
                index = int(((start + finish)/2))
            if (finish - start ==1 and nums[index] != target):
                return -1
        return -1


a = Solution()
print(a.search([-1,2,3], 0))
