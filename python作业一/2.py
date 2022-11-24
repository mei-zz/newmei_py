#2题
# import math
# A=input().split(",")
# print(A)
# for i in A:
#     print(int((math.sqrt((2*50*int(i))//30))))
def func1(n):
    if n==1:
        return 1
    else:
        return n *func1(n-1)

print(func1(8))