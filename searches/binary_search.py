from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if (len(nums) == 0):
            return -1
        index = int(len(nums)/2)
        start = 0
        finish = len(nums) - 1
        while (start <= finish):
            if (nums[index] == target):
                return index
            elif (nums[index] < target):
                index += 1
                start = index
            else:
                index -= 1
                finish = index

        return -1
