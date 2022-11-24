# 第8题


'''
num = int(input("输入你的学号："))
Steps = 13+15
a = [1,2,4]
for i in range(4,Steps+1):
    c = len(a)
    a.append(a[c-3]+a[c-2]+a[c-1])
c = len(a)
print(f"台阶数为{Steps}时，共有{a[c-1]}种跳法")
'''

import sympy
from scipy.special import comb, perm
X=13+15
a,b,c=sympy.symbols("a b c")
all=0
list = []
for a in range(0,X+1):
    for b in range(0,X//2+1):
        for c in range(0,X//3+1):
            if(a+2*b+3*c==X):
                all+=1
                list.append([a+b+c])    #保存一共需要的所有步数
print(list)
all=0
for i in list:
    print(i[0])
    all+=comb(28,i[0])
print(all)
