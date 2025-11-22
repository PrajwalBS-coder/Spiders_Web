nums = [1,2,3,4]
divide=3
c=0
for i in range(len(nums)):
    if(nums[i]%divide==0):
        c+=1
print(abs(c-len(nums)))