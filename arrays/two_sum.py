class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if (d.get(target - nums[i]) is not None):
                return [i, d.get(target-nums[i])]
            d[nums[i]] =  i
