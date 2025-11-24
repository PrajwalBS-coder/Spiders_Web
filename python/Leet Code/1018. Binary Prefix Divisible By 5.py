nums = [1,1,1]
ans=[]
prefix = 0
for num in nums:
    print(prefix << 1)
    prefix = ((prefix << 1) + num) % 5
    ans.append(prefix == 0)
print(ans)