import math
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        gcd = math.gcd(length, k)
        for i in range(gcd):
            saved = None
            start = 0
            j = i
            waiting = None
            while(j != i or start == 0):
                start = 1
                j += k
                while (j > length - 1):
                    j -= length
                saved = nums[j]
                if (waiting is not None):
                    nums[j] = waiting
                else:
                    nums[j] = nums[i]
                waiting = saved
