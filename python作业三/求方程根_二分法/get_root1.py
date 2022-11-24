import numpy as np
import matplotlib.pyplot as plt
A=3
B=A%3+1
# 定义 x 变量的范围 (-3，3) 数量
x = np.linspace(-3.14, 6.28, 50)
y = np.exp(-x)-np.sin(B*x)

# Figure 并指定大小
plt.figure(num=3, figsize=(8, 10))
plt.plot(x, y, color='red', linewidth=1.0, linestyle='--')
plt.xlim(0, 7)
plt.ylim(-2, 3)
plt.xlabel('x')
plt.ylabel('y')

# 设置坐标轴刻度线
new_ticks = np.linspace(-1, 7, 10)
plt.xticks(new_ticks)
# 设置坐标轴 gca() 获取坐标轴信息
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 移动坐标轴
# 将 bottom 即是 x 坐标轴设置到 y=0 的位置。
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
# 将 left 即是 y 坐标轴设置到 x=0 的位置。
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
# 设置标签
ax.set_title('np.exp(-x)-np.sin(1*x)', fontsize=14, color='r')
plt.show()








