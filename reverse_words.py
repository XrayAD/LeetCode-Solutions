class Solution:
    def reverseWords(self, s: str) -> str:
        word = ""
        cache = ""
        for i in range(len(s)):
            if  s[i] == " ":
                word = word + cache + " "
                cache = ""
            else:
                cache = s[i] + cache
        word += cache
        return word
