class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        saver = [None, 0]
        for num in nums:
            if num == saver[0]:
                saver[1] += 1
            elif saver[0] == None:
                saver[0] = num
                saver[1] = 1
            else:
                saver[1] -= 1
                if saver[1] == 0:
                    saver[0] = None
        return saver[0]
