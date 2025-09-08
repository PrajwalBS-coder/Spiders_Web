n=11
for  i in range(1,n):
    if '0' in str(i) or '0' in str(n-i):
        continue
    elif i+(n-i)==n:
        print([i,(n-i)])
        break
