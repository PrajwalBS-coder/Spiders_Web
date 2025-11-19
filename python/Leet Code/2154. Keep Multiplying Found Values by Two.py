nums = [8,19,4,2,15,3]
original = 2
nums.sort()

for i in nums:
    if i == original:
        original *=2

print(original)