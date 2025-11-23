all_combos = []
from itertools import combinations
def maximumSum(nums):
    for r in range(1, len(nums)+1):
        for combo in combinations(nums, r):
            all_combos.append(sum(list(combo)))
    return all_combos
    


nums = [4]
devide=3
nums.sort()
maxsum=maximumSum(nums)
maxsum.sort(reverse=True)
for i in maxsum:
    if(i%devide==0):
        print(i)
        break
else:
    print(0)
