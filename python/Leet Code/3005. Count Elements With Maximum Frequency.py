# nums = [1,2,3,4,5]
# maxc=1
# c=0
# for i in nums:
#     if(nums.count(i)>maxc):
#         maxc=nums.count(i)
# for i in nums:
#     if(nums.count(i)==maxc):
#         c+=1
# print(c)


class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        freq = [0] * 101#Generating Empty List of size 101
        # print(freq,len(freq))
        max = 0
        res = 0
        for n in nums:
            freq[n] += 1#incrementing the frequency
            f = freq[n]
            # print(f,freq)
            if f > max:#
                max = f
                res = f
            elif f == max:
                res += f
        return res

nums =  [1,2,2,3,1,4]
print(Solution().maxFrequencyElements(nums))