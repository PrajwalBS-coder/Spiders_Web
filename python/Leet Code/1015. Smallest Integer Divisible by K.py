k = 5
# binary_str="0"
# for i in range(k-1):
#     binary_str+="1"
# # print(int(binary_str,2))
# print(binary_str)
# integer_num=int(binary_str,2)
# print(integer_num)
# if integer_num%k==0:
#     print(integer_num)
#     print(k)
# # print(int(binary_str,2)%k)
# else:
#     print(-1)

r =0 
for i in range(k):
    r= (r * 10)+1 
    print(r)
    r = r%k
    print(r)
    if r==0:
        print (i+1)
print (-1)