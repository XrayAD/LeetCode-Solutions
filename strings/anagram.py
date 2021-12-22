from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(Counter(s) == Counter(t))

a = Solution()
a.isAnagram("abc", "cba")
