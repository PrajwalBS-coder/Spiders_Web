digits = [1,2,3]

st=""
for i in digits:
    st+=str(i)
l=(int(st)+1)

print([int(i) for i in str(l)])