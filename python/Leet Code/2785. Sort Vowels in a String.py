# s =  "lYmpH"
# vowels = "aeiouAEIOU"
# v=[]
# for i in range(len(s)):
#     if s[i] in vowels:
#         v.append(s[i])
# v.sort()
# for i in range(len(s)):
#     if s[i] in vowels:
#         s=s[:i]+v.pop(0)+s[i+1:]
# print(s)


class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        v=[]
        for i in range(len(s)):
            if s[i] in vowels:
                v.append(s[i])
        v.sort()
        for i in range(len(s)):
            if s[i] in vowels:
                s=s[:i]+v.pop(0)+s[i+1:]
        return s
    
sol=Solution()
print(sol.sortVowels("lYmpH"))