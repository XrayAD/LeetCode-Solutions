class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        current = 0
        dic = {}
        for i in range(len(s)):
            char = s[i]
            if dic.get(char) is None:
                current += 1
                longest = max(current, longest)
            else:
                if i - dic[char] <= current:
                    current = i - dic[char]
                else:
                    current += 1
            longest = max(current, longest)
            dic[char] = i
        return longest
