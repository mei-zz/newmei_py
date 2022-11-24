# #迭代器使用
# class mask:
#     def __init__(self):
#         num = int(input('输入一个数字：'))
#         self.num=num
#     def use(self):
#         iter_obj = iter(list(range(0, self.num + 1)))
#         for i in range(0,self.num+1):
#             res = next(iter_obj)
#             if res%7==0:
#                 print(res, end=" ")
# B=mask()
# B.use()
def fun(n):
    if n==0 or n==1:
        return 1
    else:
        return(n*fun(n-1))
num=int(input('请输入你学号后两位：'))
x=num+15
NumSteps=0
for a in range(0,x+1):
    for b in range(0,x//2+1):
        for c in range(0,x//3+1):
            if(a+2*b+3*c==x):
                if (a==b==0 or a==c==0 or b==c==0 ):
                    NumSteps+=1
                else:
                    NumSteps+=fun(a+b+c)/(fun(a)*fun(b)*fun(c))  #有重复元素情况下进行的全排列
print('所有上台阶的方法种数为',NumSteps,'种。')
