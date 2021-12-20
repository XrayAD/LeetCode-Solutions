class Solution:
    def longestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        biggest = ""
        num = 0
        T = [0]*(len(s)+1)*(len(s)+1)
        for i in range(len(s)):
            for j in range(len(s)):
                if s[i] == rev[j]:
                    new_num = 1+i + (len(s)+1)*(j+1)
                    T[new_num] = T[i + (len(s)+1)*j] + 1
                    val = T[new_num]
                    if val > num:
                        #print("here")
                        #print(val)
                        #print(j)
                        num = val
                        biggest = rev[j-val+1:j+1]
        print(T)
        return biggest

a = Solution()
print(a.longestPalindrome("aacabdkacaa"))
