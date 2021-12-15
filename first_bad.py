class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first_bad = n
        start = 0
        finish  = n
        index = int((n+1)/2)
        while (start <= finish):
            if (isBadVersion(index)):
                if (index < first_bad):
                    first_bad = index
                finish = index - 1
                index = int((start + finish + 1)/2)
            else:
                start = index + 1
                index = int((start + finish + 1)/2)
        return(first_bad)
