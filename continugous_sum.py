class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        top = nums[0]
        prev_sum = 0
        for num in nums:
            top = max(num, num+prev_sum, top)
            prev_sum = num+prev_sum
            if prev_sum < 0:
                prev_sum = 0
        return top
