s = "pps"
v='aeiou'
c='qwrtypsdfghjklzxcvbnm'
vc=0
cc=0
for i in s:
    if i in v:
        if vc<s.count(i):
            vc=s.count(i)
    else:
        if cc<s.count(i):
            cc=s.count(i)
print(cc+vc)