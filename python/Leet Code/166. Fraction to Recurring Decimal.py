numerator = 4
denominator = 333
l=(str(numerator/denominator).split(".")[1])
# print(l)
if l=="0":
    print(str(int(numerator/denominator)))
elif len(l)>2:
    l="".join(dict.fromkeys(l))
    print(str(int(numerator/denominator))+"."+"("+l+")")
