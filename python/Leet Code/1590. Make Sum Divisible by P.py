nums = [6,3,5,2]
p = 9
# re=nums[::]
# nums.sort()
# print(nums)
# re=nums
# while(sum(nums)%p!=0):
#     nums=nums[:len(nums)-1:]
#     print(nums)
# print(len(re)-len(nums))


r=sum(nums)
r=r%p
print(r)
if r in nums:
    nums.remove(r)
else:
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            print(nums[i],nums[j])
            if nums[i]+nums[j]==r:
                nums.remove(nums[i])
                break
print(nums)