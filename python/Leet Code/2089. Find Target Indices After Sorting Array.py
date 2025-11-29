nums = [1,2,5,2,3]
target = 2
nums=sorted(nums)
l=[]
for i in range(len(nums)):
    if nums[i]==target:
        l.append(i)
print(l)