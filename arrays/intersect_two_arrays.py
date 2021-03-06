class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersect = []
        nums1.sort()
        nums2.sort()
        len1 = len(nums1)
        len2 = len(nums2)
        i = j = 0
        while i<len(nums1) and j <len(nums2):
            if (nums1[i] == nums2[j]):
                intersect.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                j +=1
        return intersect
