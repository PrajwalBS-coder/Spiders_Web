text = "leet code"
brokenLetters = "lt"
l=text.split(" ")
bk=set(brokenLetters)
print(bk)
count=0
# for i in l:
#     bkw=False
#     for j in bk:
#         if j in i:
#             bkw=True 
#             break
#     if not bkw:
#         c+=1
# print(c)
for word in l:
    bad = False
    for c in word:
        if c in bk:
            bad = True
            break
    if not bad:
        count += 1
print(count)
