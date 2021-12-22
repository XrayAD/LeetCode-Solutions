from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        first = Counter(s1)
        i = 0
        if len(s1) > len(s2):
            return False
        init = Counter(s2[0:len(s1)])
        while(True):
            print("here")
            print(i)
            if (init == first):
                return True
            if (i + len(s1)) == len(s2):
                return False
            init = init - Counter(s2[i])
            init = init + Counter(s2[i+len(s1)])
            i += 1

a = Solution()
print(a.checkInclusion("adc", "dcda"))
