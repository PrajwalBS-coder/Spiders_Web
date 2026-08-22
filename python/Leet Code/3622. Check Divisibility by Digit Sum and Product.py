import math
n = 10
l=digits = [int(digit) for digit in str(n)]
print(l)
s1=(sum(l))
s2=(math.prod(l))
if n==(s1+s2):
    print(True)
else:
    print(False)