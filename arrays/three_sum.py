from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = {}
        c = {}
        my_list = []
        for i in range(len(nums)):
            d[nums[i]] = []
            c[nums[i]] = c.get(nums[i], []) + [i]
        for i in range(len(nums)):
            x = nums[i]
            for j in range(i+1, len(nums)):
                y = nums[j]
                if d.get(-x -y) is not None and y not in d[x] and check_index(c.get(-x -y), j+1):
                    my_list.append([x, y, -x - y])
                    d[y] = d[y] + [x] + [-x - y]
                    d[x] = d[x] + [y] + [-x - y]
                    d[-x-y] = d[-x-y] + [x] + [y]
        return my_list


def check_index(nums: List[int], index):
    for num in nums:
        if num >= index:
            return True
    return False
