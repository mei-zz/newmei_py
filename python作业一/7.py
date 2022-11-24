#局部变量
def func1():
	a = 1 # 1.定义一个局部变量
	print(a)
	a = 20# 3.修改局部变量
	print(a)
func1()
# print(a)  函数外部无法调用
#************************************#
#全局变量
b = 10 # (1) 定义一个全局变量
print(b)
b = 30# (3) 修改一个全局变量
print(b)
def func2():
	print(b)
func2()
