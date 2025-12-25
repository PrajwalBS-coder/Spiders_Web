happiness = [2,98,45]
k = 1
happiness.sort()
total_happiness =[]
for i in range(k):
    total_happiness.append(happiness[-1])
    happiness.pop()
    happiness=list(map(lambda x: x - 1, happiness))
print((total_happiness))
print(sum(total_happiness))