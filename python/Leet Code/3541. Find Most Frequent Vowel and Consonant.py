# s = "pps"
# v='aeiou'
# c='qwrtypsdfghjklzxcvbnm'
# vc=0
# cc=0
# for i in s:
#     if i in v:
#         if vc<s.count(i):
#             vc=s.count(i)
#     else:
#         if cc<s.count(i):
#             cc=s.count(i)
# print(cc+vc)


from collections import Counter
s = "pps"
v='aeiou'
mp = Counter(s)#mp={'p':2,'s':1}
print(mp)
vc = max((mp[ch] for ch in mp if ch in v), default=0)
cc = max((mp[ch] for ch in mp if ch not in v), default=0)
print(cc+vc)