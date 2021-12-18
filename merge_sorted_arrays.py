class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        fp = m -1
        sp = n - 1
        while (sp >= 0):
            if (fp < 0):
                nums1[sp] = nums2[sp]
                sp -= 1
            elif (nums1[fp] > nums2[sp] or sp < 0):
                nums1[fp+sp + 1] = nums1[fp]
                fp-=1
            else:
                nums1[fp+sp + 1] = nums2[sp]
                sp-=1
