from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:#if list length is greater than 1
            new_nums = list()
            for i in range(len(nums) - 1):
                new_nums.append((nums[i] + nums[i + 1]) % 10)
            nums = new_nums
        return nums[0]
    
obj=Solution()
print(obj.triangularSum([4,2,1,3]))