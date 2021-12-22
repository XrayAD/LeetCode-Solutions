class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = OrderedDict()
        for i, char in enumerate(s):
            if d.get(char) is None:
                d[char] = i
            else:
                d[char] = len(s)
        for key, val in d.items():
            if val < len(s):
                return val
        return -1

    def firstUniqChar1(self, s):
        """
        :type s: str
        :rtype: int
        """

        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letters if s.count(l) == 1]
        print(index)
        return min(index) if len(index) > 0 else -1

a = Solution()
a.firstUniqChar1("leetcode")
