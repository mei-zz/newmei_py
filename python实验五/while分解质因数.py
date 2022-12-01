# 未使用递归分解质因数
"""
编写一个函数，利用“递归方法”对输入的参数分解质因数，
并将结果用append方法加入到一个列表中，分解完毕后，
利用for循环遍历，将列表中元素逐个打印出来；
"""
n=int(input("请输入需要分解的数字："))
print("{} =".format(n),end=' ')
while n>1:
    for i in range(2,n+1):
        if n%i==0:
            n=int(n/i)
            if n==1:
                print(i)
            else:
                print("{} *".format(i),end=' ')
            break