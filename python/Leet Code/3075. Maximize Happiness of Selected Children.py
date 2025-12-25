happiness = [12,1,42]
k = 3
# for i in range(k):
#     if happiness[-1]<=0:
#         continue
#     total_happiness.append(happiness[-1])
#     happiness.pop()
#     happiness=list(map(lambda x: x - 1, happiness))
# print((total_happiness))
# print(sum(total_happiness))

happiness.sort(reverse=True)
total_happiness_sum = 0
turns = 0
for i in range(k):
    total_happiness_sum += max(happiness[i] - turns, 0)
    turns += 1
print( total_happiness_sum)