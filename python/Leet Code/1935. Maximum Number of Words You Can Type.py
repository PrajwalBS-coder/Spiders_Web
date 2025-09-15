text = "leet code"
brokenLetters = "lt"
l=text.split(" ")
bk=set(brokenLetters)
print(bk)
c=0
for i in l:
    bkw=False
    for j in bk:
        if j in i:
            bkw=True 
            break
    if not bkw:
        c+=1
print(c)
