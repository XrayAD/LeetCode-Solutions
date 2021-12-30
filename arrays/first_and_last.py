class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        finish = len(nums) - 1
        while (start <= finish):
            mid = int((start + finish)/2)
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                finish = mid - 1
            else:
                left = self.searchLeft(nums, start, mid - 1, target, mid)
                right = self.searchRight(nums, mid+1, finish, target, mid)
                return [left, right]
        return [-1, -1]
    def searchLeft(self, nums: List[int], start, finish, target, last):
        if start > finish:
            return last
        mid = int((start + finish)/2)
        if nums[mid] < target:
            return self.searchLeft(nums, mid +1, finish, target, last)
        else:
            return self.searchLeft(nums, start, mid - 1, target, mid)

    def searchRight(self, nums: List[int], start, finish, target, last):
        if start > finish:
            return last
        mid = int((start + finish)/2)
        if nums[mid] > target:
            return self.searchRight(nums, start, mid - 1, target, last)
        else:
            return self.searchRight(nums, mid+1, finish, target, mid)
