nums = [1,2,3,4,5]
maxc=1
c=0
for i in nums:
    if(nums.count(i)>maxc):
        maxc=nums.count(i)
for i in nums:
    if(nums.count(i)==maxc):
        c+=1
print(c)