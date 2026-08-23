import math
num = "5023"
if "?" in num:
    num = num.replace("?", "9")
s1,s2=num[:len(num)//2],num[len(num)//2:]
sum1=[int(digit) for digit in str(s1)]
sum2=[int(digit) for digit in str(s2)]
print(s1)
print(s2)
print(type(s1),type(s2))
if (sum(sum1)) == (sum(sum2)):
    print(False)
else:
    print(True)