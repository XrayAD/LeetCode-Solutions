from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_counter = 0
        for i in range(len(nums)):
            if (nums[i]) == 0:
                zero_counter+=1
            else:
                nums[i-zero_counter] = nums[i]
        for i in range(zero_counter):
            nums[-(i+1)] = 0
